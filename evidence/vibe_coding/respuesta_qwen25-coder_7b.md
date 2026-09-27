# qwen2.5-coder:7b · 2026-09-27T13:24:02 · 104.71 s

Aquí tienes un script en Python que cumple con los requisitos que has especificado:

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Any

# Definición de tipos para la respuesta de la API
class ApiResponse:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def get_hourly_data(self) -> List[float]:
        return self.data['hourly']['temperature_2m']

    def get_timestamps(self) -> List[str]:
        return self.data['hourly']['time']

def fetch_weather_data() -> ApiResponse:
    url = "https://api.open-meteo.com/v1/forecast?latitude=5.0689&longitude=-75.5174&past_days=7&hourly=temperature_2m"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error al obtener los datos: {response.status_code}")
    
    try:
        data = response.json()
        if 'hourly' not in data or 'temperature_2m' not in data['hourly']:
            raise Exception("La respuesta JSON no contiene las llaves esperadas")
        return ApiResponse(data)
    except ValueError:
        raise Exception("Error al decodificar la respuesta JSON")

def process_data(api_response: ApiResponse) -> pd.DataFrame:
    timestamps = api_response.get_timestamps()
    temperatures = api_response.get_hourly_data()
    
    # Convertir las fechas a formato datetime
    timestamps = pd.to_datetime(timestamps)
    
    # Crear el DataFrame
    df = pd.DataFrame({
        'Fecha': timestamps,
        'Temperatura': temperatures
    })
    
    # Verificar valores nulos
    if df.isnull().values.any():
        raise Exception("Se encontraron valores nulos en los datos")
    
    return df

def calculate_statistics(df: pd.DataFrame) -> None:
    mean_temp = df['Temperatura'].mean()
    median_temp = df['Temperatura'].median()
    min_temp = df['Temperatura'].min()
    max_temp = df['Temperatura'].max()
    
    print(f"Media: {mean_temp:.2f}°C")
    print(f"Mediana: {median_temp:.2f}°C")
    print(f"Mínimo: {min_temp:.2f}°C")
    print(f"Máximo: {max_temp:.2f}°C")

def plot_temperature(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(df['Fecha'], df['Temperatura'], marker='o', linestyle='-', color='b')
    plt.title('Temperatura a lo largo del tiempo en Manizales')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('temperatura_manizales.png')
    plt.show()

def main() -> None:
    try:
        api_response = fetch_weather_data()
        df = process_data(api_response)
        calculate_statistics(df)
        plot_temperature(df)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Explicación técnica:

1. **Definición de tipos**: Se definen clases y tipos para la respuesta de la API y para manejar los datos de manera más estructurada.

2. **Consumo de la API**: La función `fetch_weather_data` realiza la solicitud a la API y valida la respuesta. Si la respuesta no es 200 o no contiene las llaves esperadas, se lanza una excepción.

3. **Procesamiento de los datos**: La función `process_data` convierte las fechas a formato `datetime`, crea un DataFrame de Pandas y verifica la presencia de valores nulos.

4. **Cálculo de estadísticas**: La función `calculate_statistics` calcula y imprime la media, mediana, valor mínimo y valor máximo de las temperaturas.

5. **Generación de gráfica**: La función `plot_temperature` genera una gráfica de línea de la temperatura a lo largo del tiempo y la guarda en un archivo PNG.

6. **Manejo de excepciones**: Se utiliza un bloque `try-except` para manejar cualquier excepción que pueda ocurrir durante el proceso.

7. **Función principal**: La función `main` coordina el flujo del programa, llamando a las funciones anteriores en el orden correcto.

Este script es completamente funcional y cumple con todos los requisitos que has especificado.
