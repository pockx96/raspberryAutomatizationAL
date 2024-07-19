from gpiozero import Button
from time import time, sleep
import requests
import json

# Configuración del botón
pin_boton = 17  # Ejemplo de pin GPIO donde está conectado el botón
mi_boton = Button(pin_boton)

# Variables para medir el tiempo
tiempo_inicio = None
lectura = 0

def medir_tiempo():
    global tiempo_inicio, lectura
    try:
        while True:
            if mi_boton.is_pressed:
                if tiempo_inicio is None:
                    tiempo_inicio = time()  # Guardar el tiempo de inicio
            else:
                if tiempo_inicio is not None:
                    tiempo_fin = time()  # Guardar el tiempo de fin
                    lectura = tiempo_fin - tiempo_inicio
                    print(f"Tiempo presionado: {lectura:.2f} segundos")
                    tiempo_inicio = None  # Reiniciar el tiempo de inicio
                    enviar_post(lectura)
            
            sleep(0.1)  # Esperar un breve periodo para evitar lecturas muy rápidas
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")

def enviar_post(lectura):
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'Lectura de botón',
        'body': f'Tiempo presionado: {lectura:.2f} segundos',
        'userId': 1
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 201:
        print('POST enviado con éxito:', response.json())
    else:
        print('Error al enviar POST:', response.status_code)

# Ejecutar la función de medición de tiempo
medir_tiempo()





