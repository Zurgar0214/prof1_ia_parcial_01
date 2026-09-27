"""Reto integrador (Componente 4): API -> JSON -> Pandas -> serie -> modelo -> métricas -> gráficas.

Autor: Juan Diego Varón Valencia (desarrollado con apoyo de IA, ver docs/uso_ia/uso_ia_componente4.md)

Uso:
    python app.py                               # consulta la API (2023-01-01 a hoy)
    python app.py --inicio 2022-01-01 --fin 2026-09-22
    python app.py --offline                     # reutiliza outputs/trm_raw.json (sin red)

Todos los resultados quedan en serie_temporal/outputs/.
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
from datetime import datetime

import matplotlib
import pandas as pd
import sklearn

import api_client
import config
import evaluation
import model
import preprocessing


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Pronóstico de la TRM USD/COP con datos de API pública.")
    p.add_argument("--inicio", default=config.FECHA_INICIO, help="Fecha inicial AAAA-MM-DD")
    p.add_argument("--fin", default=config.FECHA_FIN, help="Fecha final AAAA-MM-DD")
    p.add_argument("--test-size", type=float, default=config.TEST_SIZE, help="Proporción final para prueba")
    p.add_argument("--ventana", type=int, default=config.VENTANA_MEDIA_MOVIL, help="Ventana de la media móvil")
    p.add_argument("--rezagos", type=int, default=config.N_REZAGOS, help="Rezagos de la regresión AR")
    p.add_argument("--horizonte", type=int, default=config.HORIZONTE, help="Próximas TRM (publicaciones) a pronosticar")
    p.add_argument("--offline", action="store_true", help="Usar el JSON guardado en lugar de llamar la API")
    return p.parse_args(argv)


def paso(n: int, texto: str) -> None:
    print(f"\n[{n}] {texto}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    out = config.OUTPUT_DIR
    out.mkdir(parents=True, exist_ok=True)

    # 1. API -> JSON --------------------------------------------------------------
    paso(1, "Obteniendo datos")
    try:
        if args.offline:
            registros, meta = api_client.cargar_json(config.RAW_JSON_PATH)
            print(f"    Modo offline: {len(registros)} registros desde {config.RAW_JSON_PATH.name}")
        else:
            registros, meta = api_client.obtener_trm(args.inicio, args.fin)
            api_client.guardar_json(registros, meta, config.RAW_JSON_PATH)
            print(f"    GET {meta['endpoint']} -> HTTP 200, {meta['registros']} registros "
                  f"en {meta['paginas']} página(s), {meta['segundos']} s")
            print(f"    Respuesta cruda guardada en outputs/{config.RAW_JSON_PATH.name}")
    except (api_client.APIError, FileNotFoundError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    # 2. JSON -> Pandas + validación ------------------------------------------------
    paso(2, "Preparando y validando datos")
    df, reporte = preprocessing.a_dataframe(registros)
    for clave, valor in reporte.como_dict().items():
        print(f"    {clave:<24} {valor}")
    serie = preprocessing.construir_serie(df)
    print(f"    Tipos: índice={serie.index.dtype}, valores={serie.dtype}")

    # 3. División temporal ----------------------------------------------------------
    paso(3, "Dividiendo entrenamiento/prueba en orden temporal")
    train, test = preprocessing.dividir_train_test(serie, args.test_size)
    assert train.index.max() < test.index.min(), "Fuga temporal: prueba antes que entrenamiento"
    print(f"    Entrenamiento: {train.index.min().date()} -> {train.index.max().date()} ({len(train)} obs.)")
    print(f"    Prueba:        {test.index.min().date()} -> {test.index.max().date()} ({len(test)} obs.)")

    # 4. Modelos --------------------------------------------------------------------
    paso(4, "Entrenando modelos y pronosticando el tramo de prueba (walk-forward, 1 paso)")
    reg = model.RegresionAutorregresiva(args.rezagos).entrenar(train)
    predicciones = {
        "Persistencia (baseline)": model.pronostico_persistencia(serie, test.index),
        f"Media móvil {args.ventana} (baseline)": model.pronostico_media_movil(serie, test.index, args.ventana),
        f"Regresión AR({args.rezagos})": reg.pronosticar_un_paso(serie, test.index),
    }
    print("    Coeficientes AR:", {k: round(v, 4) for k, v in reg.coeficientes().items()})

    # 5. Métricas -------------------------------------------------------------------
    paso(5, "Métricas sobre el tramo de prueba")
    metricas = evaluation.tabla_metricas(test, predicciones)
    print(metricas.to_string(index=False))
    metricas.to_csv(out / "metricas.csv", index=False)
    comparacion = pd.concat({"real": test, **predicciones}, axis=1)
    comparacion.to_csv(out / "predicciones_prueba.csv", index_label="fecha", float_format="%.2f")

    # 6. Pronóstico futuro (modelo re-entrenado con toda la historia) -------------------
    paso(6, f"Pronóstico de las próximas {args.horizonte} TRM publicadas")
    reg_final = model.RegresionAutorregresiva(args.rezagos).entrenar(serie)
    # La última TRM ya rige hasta su `vigenciahasta` (p. ej. la del sábado cubre hasta el lunes),
    # así que la primera fecha desconocida es el día siguiente. Las vigencias nuevas empiezan
    # de martes a sábado (la del sábado cubre sábado-domingo-lunes).
    inicio_futuro = df["vigenciahasta"].max() + pd.Timedelta(days=1)
    fechas_futuras = pd.bdate_range(inicio_futuro, periods=args.horizonte, freq="C",
                                    weekmask="Tue Wed Thu Fri Sat")
    print(f"    Última TRM conocida rige hasta {df['vigenciahasta'].max().date()}")
    futuro = reg_final.pronosticar_futuro(serie, args.horizonte, fechas_futuras)
    print(futuro.to_string())
    futuro.to_csv(out / "pronostico_futuro.csv", index_label="fecha")

    # 7. Gráficas -------------------------------------------------------------------
    paso(7, "Generando gráficas")
    evaluation.graficar_serie(serie, train, test, out / "01_serie_train_test.png", args.ventana)
    evaluation.graficar_real_vs_pred(test, predicciones, out / "02_real_vs_prediccion.png")
    evaluation.graficar_errores(test, predicciones, out / "03_errores.png")
    evaluation.graficar_pronostico(serie, futuro, out / "04_pronostico_futuro.png")
    print("    01_serie_train_test.png, 02_real_vs_prediccion.png, 03_errores.png, 04_pronostico_futuro.png")

    # 8. Registro de la ejecución (evidencia reproducible) ----------------------------
    resumen = {
        "ejecutado_en": datetime.now().isoformat(timespec="seconds"),
        "modo": "offline" if args.offline else "api",
        "api": meta,
        "parametros": vars(args),
        "calidad_datos": reporte.como_dict(),
        "entrenamiento": [str(train.index.min().date()), str(train.index.max().date()), len(train)],
        "prueba": [str(test.index.min().date()), str(test.index.max().date()), len(test)],
        "metricas": metricas.to_dict(orient="records"),
        "coeficientes_ar": reg.coeficientes(),
        "entorno": {
            "python": platform.python_version(),
            "sistema": platform.platform(),
            "pandas": pd.__version__,
            "scikit-learn": sklearn.__version__,
            "matplotlib": matplotlib.__version__,
        },
    }
    with (out / "resumen_ejecucion.json").open("w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2, default=str)
    print(f"\nListo. Resultados en {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
