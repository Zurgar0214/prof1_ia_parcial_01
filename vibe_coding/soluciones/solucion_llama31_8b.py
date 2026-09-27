# Código generado por Llama 3.1 8B (Ollama, local generalista) SIN MODIFICACIONES (extraído de ../respuestallama3.1.txt).
# Prompt: ../promptUtilizado.txt
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# 1. Consumir API pública de Open-Meteo
try:
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 5.0689,
        'longitude': -75.5174,
        'past_days': 7,
        'hourly': 'temperature_2m'
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # Lanzar excepción si el código HTTP no es 200
except requests.RequestException as e:
    raise Exception(f'Error en la petición HTTP: {e}')

# 2. Verificar que la respuesta sea correcta
try:
    data = response.json()
    assert 'hourly' in data and 'temperature_2m' in data['hourly']
except (ValueError, AssertionError) as e:
    raise Exception(f'Error en la respuesta: {e}')

# 3. Procesar datos y crear DataFrame
data_hourly = data['hourly']
timestamp = pd.to_datetime(data_hourly['time'])
temperatures = data_hourly['temperature_2m']

df = pd.DataFrame({'timestamp': timestamp, 'temperature': temperatures})
assert not df.isnull().values.any(), 'Hay valores nulos en los datos'

# 4. Calcular y mostrar estadísticas
stats = df['temperature'].agg(['mean', 'median', 'min', 'max'])
print(stats)

# 5. Generar gráfica
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['temperature'])
plt.title('Temperatura en Manizales')
plt.xlabel('Fecha y hora')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.savefig('temperatura_manizales.png')
plt.show()
