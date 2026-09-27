"""Mide cuánto tarda cada modelo LOCAL en generar la solución del Componente 3.

Envía el mismo prompt (promptUtilizado.txt) a los modelos de Ollama y guarda
el tiempo, los tokens y el código generado como evidencia.

Uso (con Ollama corriendo):  python vibe_coding/medir_generacion.py
Salida: evidence/vibe_coding/tiempos_generacion.csv y respuestas_<modelo>.md
"""
from __future__ import annotations

import csv
import time
from datetime import datetime
from pathlib import Path

import requests

MODELOS = ["llama3.1", "qwen2.5-coder:7b"]
URL = "http://localhost:11434/api/generate"
BASE = Path(__file__).resolve().parent
SALIDA = BASE.parent / "evidence" / "vibe_coding"


def main() -> None:
    prompt = (BASE / "promptUtilizado.txt").read_text(encoding="utf-8")
    SALIDA.mkdir(parents=True, exist_ok=True)
    filas = []
    for modelo in MODELOS:
        print(f"-> {modelo} generando...", end=" ", flush=True)
        t0 = time.perf_counter()
        r = requests.post(URL, timeout=900, json={
            "model": modelo, "prompt": prompt, "stream": False, "options": {"temperature": 0.2}})
        r.raise_for_status()
        d = r.json()
        total = time.perf_counter() - t0
        tokens = d.get("eval_count", 0)
        eval_s = d.get("eval_duration", 0) / 1e9
        fila = {
            "fecha": datetime.now().isoformat(timespec="seconds"),
            "modelo": modelo,
            "segundos_total": round(total, 2),
            "segundos_carga": round(d.get("load_duration", 0) / 1e9, 2),
            "tokens_generados": tokens,
            "tokens_por_s": round(tokens / eval_s, 2) if eval_s else "",
        }
        filas.append(fila)
        nombre = modelo.replace(":", "_").replace(".", "")
        (SALIDA / f"respuesta_{nombre}.md").write_text(
            f"# {modelo} · {fila['fecha']} · {fila['segundos_total']} s\n\n{d.get('response', '')}\n",
            encoding="utf-8")
        print(f"{fila['segundos_total']} s, {tokens} tokens")

    with (SALIDA / "tiempos_generacion.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    print(f"Guardado en {SALIDA}")


if __name__ == "__main__":
    main()
