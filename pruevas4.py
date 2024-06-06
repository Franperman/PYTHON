import time
import threading

def miFuncion(numero, delay, bucle):
    # Función que será ejecutada por los hilos
    while bucle.is_set():
        print(f"Función {numero}, en ejecución cada {delay} segundos")
        time.sleep(delay)

# Evento que controlará el bucle de ejecución de los hilos
bucle = threading.Event()
bucle.set()  # Inicia el evento, permitiendo que los hilos corran

# Creación de hilos, cada uno ejecutando miFuncion con diferentes argumentos
hilo1 = threading.Thread(target=miFuncion, args=(1, 1, bucle))
hilo2 = threading.Thread(target=miFuncion, args=(2, 3, bucle))
hilo3 = threading.Thread(target=miFuncion, args=(3, 6, bucle), daemon=True)  # Daemon thread
hilo4 = threading.Thread(target=miFuncion, args=(4, 12, bucle), daemon=True) # Daemon thread

# Iniciar los hilos
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

try:
    # Bucle principal que imprime cada 10 segundos
    while True:
        print("Hilo principal")
        time.sleep(10)
except KeyboardInterrupt:
    # Cuando se interrumpe la ejecución (Ctrl+C), se limpian los recursos
    print("Saliendo.......")
    bucle.clear()  # Detiene los hilos
    hilo1.join()  # Espera a que hilo1 termine
    hilo2.join()  # Espera a que hilo2 termine
    print("Ejecución finalizada")
