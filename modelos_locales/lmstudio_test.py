import time
import requests

def test_lmstudio():
    url = "http://localhost:1234/v1/chat/completions"
    
    payload = {
        "messages": [
            {"role": "system", "content": "Eres un asistente de software enfocado en escribir código limpio y tipado en Python."},
            {"role": "user", "content": "Escribe una función en Python para calcular la media móvil de una lista de floats con una ventana de tamaño k."}
        ],
        "temperature": 0.2,
        "max_tokens": 512
    }

    print("Enviando solicitud a LM Studio (API Local: 1234)...")
    start_time = time.time()
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        elapsed_time = time.time() - start_time
        answer = data["choices"][0]["message"]["content"]
        
        print(f"Respuesta recibida en {elapsed_time:.2f} segundos.\n")
        print("--- RESPUESTA GENERADA ---")
        print(answer)
        print("---------------------------")
        
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a LM Studio. Verifique que el servidor local esté iniciado en el puerto 1234.")

if __name__ == "__main__":
    test_lmstudio()