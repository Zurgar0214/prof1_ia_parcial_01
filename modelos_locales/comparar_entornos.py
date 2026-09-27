"""Envía el MISMO conjunto de consultas a Ollama y a LM Studio y registra métricas.

Cubre las actividades 5 y 6 del Componente 2:
  5. Conjunto equivalente de consultas en ambos entornos.
  6. Registro de modelo, cuantización, memoria observada y tiempo de respuesta.

Requisitos previos:
  - Ollama corriendo (http://localhost:11434) con: ollama pull llama3.1 / qwen2.5-coder:7b
  - LM Studio con un modelo cargado y el servidor local iniciado (Developer -> Start Server, puerto 1234)

Uso:
  python comparar_entornos.py                 # ambos entornos
  python comparar_entornos.py --solo ollama   # solo Ollama
  python comparar_entornos.py --solo lmstudio # solo LM Studio

Salida: ../evidence/modelos_locales/resultados_entornos.csv y respuestas_entornos.md
"""
from __future__ import annotations

import argparse
import csv
import platform
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

OLLAMA_URL = "http://localhost:11434"
LMSTUDIO_URL = "http://localhost:1234/v1"
OLLAMA_MODELOS = ["llama3.1", "qwen2.5-coder:7b"]  # generalista y de código
TIMEOUT = 600  # segundos: en CPU un modelo 7-8B puede tardar más de un minuto
TEMPERATURA = 0.2

PROMPTS: list[tuple[str, str]] = [
    ("general", "Explica en máximo 5 líneas qué es una serie temporal y da un ejemplo del mundo financiero."),
    ("codigo_generar", "Escribe una función en Python para calcular la media móvil de una lista de floats "
                       "con una ventana de tamaño k. Incluye tipado y manejo de errores."),
    ("codigo_explicar", "Explica qué hace este código y si tiene algún error:\n"
                        "def f(xs, k):\n    return [sum(xs[i:i+k])/k for i in range(len(xs))]"),
]

SALIDA = Path(__file__).resolve().parents[1] / "evidence" / "modelos_locales"


def _ollama_memoria(modelo: str) -> tuple[str, str]:
    """Consulta /api/ps: memoria total del modelo cargado y cuánta está en VRAM."""
    try:
        for m in requests.get(f"{OLLAMA_URL}/api/ps", timeout=10).json().get("models", []):
            if m["name"].startswith(modelo.split(":")[0]):
                total = m.get("size", 0) / 1e9
                vram = m.get("size_vram", 0) / 1e9
                return f"{total:.2f}", f"{vram:.2f}"
    except requests.RequestException:
        pass
    return "", ""


def _ollama_info(modelo: str) -> tuple[str, str]:
    """Consulta /api/show: tamaño en parámetros y nivel de cuantización."""
    try:
        d = requests.post(f"{OLLAMA_URL}/api/show", json={"model": modelo}, timeout=10).json()["details"]
        return d.get("parameter_size", ""), d.get("quantization_level", "")
    except (requests.RequestException, KeyError):
        return "", ""


def consultar_ollama(modelo: str, prompt: str) -> dict[str, Any]:
    t0 = time.perf_counter()
    r = requests.post(f"{OLLAMA_URL}/api/generate", timeout=TIMEOUT, json={
        "model": modelo, "prompt": prompt, "stream": False, "options": {"temperature": TEMPERATURA}})
    r.raise_for_status()
    d = r.json()
    total = time.perf_counter() - t0
    tokens = d.get("eval_count", 0)
    eval_s = d.get("eval_duration", 0) / 1e9
    params, quant = _ollama_info(modelo)
    mem_total, mem_vram = _ollama_memoria(modelo)
    return {
        "entorno": "Ollama", "modelo": modelo, "parametros": params, "cuantizacion": quant,
        "segundos_total": round(total, 2), "segundos_carga": round(d.get("load_duration", 0) / 1e9, 2),
        "tokens_salida": tokens, "tokens_por_s": round(tokens / eval_s, 2) if eval_s else "",
        "memoria_modelo_gb": mem_total, "memoria_en_vram_gb": mem_vram, "respuesta": d.get("response", ""),
    }


def consultar_lmstudio(prompt: str) -> dict[str, Any]:
    modelos = requests.get(f"{LMSTUDIO_URL}/models", timeout=10).json().get("data", [])
    if not modelos:
        raise RuntimeError("LM Studio no tiene ningún modelo cargado.")
    modelo = modelos[0]["id"]
    t0 = time.perf_counter()
    r = requests.post(f"{LMSTUDIO_URL}/chat/completions", timeout=TIMEOUT, json={
        "model": modelo, "messages": [{"role": "user", "content": prompt}], "temperature": TEMPERATURA})
    r.raise_for_status()
    d = r.json()
    total = time.perf_counter() - t0
    tokens = d.get("usage", {}).get("completion_tokens", 0)
    return {
        "entorno": "LM Studio", "modelo": modelo, "parametros": "", "cuantizacion": "(ver LM Studio)",
        "segundos_total": round(total, 2), "segundos_carga": "",
        "tokens_salida": tokens, "tokens_por_s": round(tokens / total, 2) if total else "",
        "memoria_modelo_gb": "(ver Administrador de tareas)", "memoria_en_vram_gb": "",
        "respuesta": d["choices"][0]["message"]["content"],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--solo", choices=["ollama", "lmstudio"])
    args = p.parse_args()

    tareas: list[tuple[str, Any]] = []
    if args.solo in (None, "ollama"):
        tareas += [(f"Ollama/{m}", lambda pr, m=m: consultar_ollama(m, pr)) for m in OLLAMA_MODELOS]
    if args.solo in (None, "lmstudio"):
        tareas.append(("LM Studio", consultar_lmstudio))

    filas: list[dict[str, Any]] = []
    for nombre, fn in tareas:
        for pid, prompt in PROMPTS:
            print(f"-> {nombre} | {pid} ...", end=" ", flush=True)
            try:
                fila = fn(prompt)
                print(f"{fila['segundos_total']} s, {fila['tokens_salida']} tokens")
            except (requests.RequestException, RuntimeError) as e:
                print(f"ERROR: {e}")
                fila = {"entorno": nombre, "modelo": nombre, "respuesta": f"ERROR: {e}"}
            fila.update({"prompt_id": pid, "fecha": datetime.now().isoformat(timespec="seconds")})
            filas.append(fila)

    SALIDA.mkdir(parents=True, exist_ok=True)
    columnas = ["fecha", "entorno", "modelo", "parametros", "cuantizacion", "prompt_id", "segundos_total",
                "segundos_carga", "tokens_salida", "tokens_por_s", "memoria_modelo_gb", "memoria_en_vram_gb"]
    with (SALIDA / "resultados_entornos.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=columnas, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    with (SALIDA / "respuestas_entornos.md").open("w", encoding="utf-8") as f:
        f.write(f"# Respuestas Ollama vs LM Studio\n\nEquipo: {platform.platform()} · "
                f"Python {platform.python_version()} · {datetime.now():%Y-%m-%d %H:%M}\n\n")
        for fila in filas:
            f.write(f"## {fila['entorno']} · {fila['modelo']} · {fila['prompt_id']}\n\n"
                    f"Tiempo: {fila.get('segundos_total', '')} s · Tokens: {fila.get('tokens_salida', '')}\n\n"
                    f"{fila['respuesta']}\n\n---\n\n")
    print(f"\nResultados guardados en {SALIDA}")


if __name__ == "__main__":
    main()
