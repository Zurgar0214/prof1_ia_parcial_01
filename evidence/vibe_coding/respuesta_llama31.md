# llama3.1 · 2026-09-27T13:22:18 · 91.41 s

Aquí te dejo el script en Python que realiza lo solicitado:
```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List

# Configuración de la API Open-Meteo
API_URL = "https://api.open-meteo.com/v1/forecast"
LATITUD = 5.0689
LONGITUD = -75.5174
DÍAS_PASADOS = 7

# Realizar la solicitud a la API
try:
    respuesta = requests.get(API_URL, params={
        "latitude": LATITUD,
        "longitude": LONGITUD,
        "past_days": DÍAS_PASADOS,
        "hourly": "temperature_2m"
    })
    respuesta.raise_for_status()  # Lanzar una excepción si la respuesta no es 200
except requests.exceptions.RequestException as e:
    print(f"Error al realizar la solicitud a la API: {e}")
    exit(1)

# Procesar la respuesta JSON
try:
    datos: Dict = respuesta.json()
    if "hourly" not in datos or "temperature_2m" not in datos["hourly"]:
        raise ValueError("La respuesta JSON no contiene las llaves 'hourly' y 'temperature_2m'")
except ValueError as e:
    print(f"Error al procesar la respuesta JSON: {e}")
    exit(1)

# Cargar los datos en un DataFrame de Pandas
df = pd.DataFrame(datos["hourly"]["temperature_2m"])

# Convertir las fechas a formato datetime
df["time"] = pd.to_datetime(df["time"])

# Verificar si existen valores nulos
if df.isnull().values.any():
    print("Existen valores nulos en el DataFrame")

# Calcular e imprimir estadísticas
media = df["temperature_2m"].mean()
mediana = df["temperature_2m"].median()
minimo = df["temperature_2m"].min()
maximo = df["temperature_2m"].max()
print(f"Media: {media:.2f}°C")
print(f"Mediana: {mediana:.2f}°C")
print(f"Valor mínimo: {minimo:.2f}°C")
print(f"Valor máximo: {maximo:.2f}°C")

# Generar y guardar una gráfica de línea
plt.figure(figsize=(10, 6))
plt.plot(df["time"], df["temperature_2m"])
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura en Manizales")
plt.grid(True)
plt.savefig("temperatura_manizales.png")
```
Este script realiza las siguientes acciones:

1. Realiza una solicitud a la API Open-Meteo para obtener las temperaturas de los últimos 7 días en Manizales.
2. Valida que la respuesta HTTP sea 200 y que el JSON contenga las llaves 'hourly' y 'temperature_2m'.
3. Carga los datos en un DataFrame de Pandas, convierte las fechas a formato datetime y verifica si existen valores nulos.
4. Calcula e imprime estadísticas sobre la temperatura (media, mediana, valor mínimo y valor máximo).
5. Genera y guarda una gráfica de línea de la temperatura a lo largo del tiempo en un archivo llamado 'temperatura_manizales.png' usando Matplotlib.

Recuerda que debes tener instaladas las bibliotecas `requests`, `pandas` y `matplotlib` para ejecutar este script.
