import json
import time
import requests

def test_ollama():
    url = "http://localhost:11434/api/generate"
    model_name = "qwen2.5-coder:7b"
    prompt = "Escribe una función en Python para calcular la media móvil de una lista de floats con una ventana de tamaño k."

    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }

    print(f"Enviando solicitud a Ollama (Modelo: {model_name})...")
    start_time = time.time()
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        elapsed_time = time.time() - start_time
        print(f"Respuesta recibida en {elapsed_time:.2f} segundos.\n")
        print("--- RESPUESTA GENERADA ---")
        print(data.get("response", ""))
        print("---------------------------")
        
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a Ollama. Verifique que el servicio esté corriendo en http://localhost:11434")

if __name__ == "__main__":
    test_ollama()