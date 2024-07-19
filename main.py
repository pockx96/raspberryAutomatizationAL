from gpiozero import Button
from time import time, sleep

# Configuración del botón
pin_boton = 17  # Ejemplo de pin GPIO donde está conectado el botón
mi_boton = Button(pin_boton)

# Variables para medir el tiempo
tiempo_inicio = None

try:
    while True:
        if mi_boton.is_pressed:
            if tiempo_inicio is None:
                tiempo_inicio = time()  # Guardar el tiempo de inicio
        else:
            if tiempo_inicio is not None:
                tiempo_fin = time()  # Guardar el tiempo de fin
                tiempo_presionado = tiempo_fin - tiempo_inicio
                print(f"Tiempo presionado: {tiempo_presionado:.2f} segundos")
                tiempo_inicio = None  # Reiniciar el tiempo de inicio
        
        sleep(0.1)  # Esperar un breve periodo para evitar lecturas muy rápidas

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")