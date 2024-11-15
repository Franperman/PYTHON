import asyncio

async def tarea1():
    print("Comenzando tarea 1")
    await asyncio.sleep(2)  # Simula una espera de 2 segundos
    print("Finalizando tarea 1")

async def tarea2():
    print("Comenzando tarea 2")
    await asyncio.sleep(1)  # Simula una espera de 1 segundo
    print("Finalizando tarea 2")

async def main():
    # Ejecutar tareas concurrentemente
    await asyncio.gather(tarea1(), tarea2())

# Ejecuta el bucle de eventos
asyncio.run(main())


import threading
import time

def tarea(nombre):
    print(f"Iniciando {nombre}")
    time.sleep(2)  # Simula una tarea que tarda 2 segundos
    print(f"Finalizando {nombre}")

# Crear varios hilos
hilo1 = threading.Thread(target=tarea, args=("Hilo 1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo 2",))

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()

print("Todos los hilos han terminado")



import asyncio
import concurrent.futures

def tarea_bloqueante():
    # Simula una tarea que toma tiempo, como una operación I/O
    print("Iniciando tarea bloqueante")
    import time
    time.sleep(3)
    print("Finalizando tarea bloqueante")

async def main():
    loop = asyncio.get_running_loop()
    # Ejecuta la tarea bloqueante en un hilo del ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, tarea_bloqueante)

asyncio.run(main())


from multiprocessing import Process
import time

def tarea_io(archivo):
    print(f"Empezando a leer {archivo}")
    time.sleep(3)  # Simula una operación de I/O
    print(f"Lectura finalizada de {archivo}")

if __name__ == "__main__":
    # Crear dos procesos que realizarán operaciones de I/O en paralelo
    proceso1 = Process(target=tarea_io, args=("archivo1.txt",))
    proceso2 = Process(target=tarea_io, args=("archivo2.txt",))
    
    proceso1.start()
    proceso2.start()
    
    proceso1.join()
    proceso2.join()
    
    print("Ambos procesos han terminado")


import threading
import time

def tarea_io(archivo):
    print(f"Empezando a leer {archivo}")
    time.sleep(3)  # Simula una operación de I/O
    print(f"Lectura finalizada de {archivo}")

hilo1 = threading.Thread(target=tarea_io, args=("archivo1.txt",))
hilo2 = threading.Thread(target=tarea_io, args=("archivo2.txt",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Ambos hilos han terminado")


import asyncio
import threading
import time

# Función que se ejecutará en un hilo
def tarea_hilo(nombre):
    print(f"Empezando tarea del hilo: {nombre}")
    time.sleep(2)  # Simula una tarea I/O bloqueante
    print(f"Terminando tarea del hilo: {nombre}")

# Función asíncrona que lanza varios hilos
async def funcion_asincrona():
    print("Lanzando hilos desde asyncio")

    hilo1 = threading.Thread(target=tarea_hilo, args=("hilo1",))
    hilo2 = threading.Thread(target=tarea_hilo, args=("hilo2",))

    hilo1.start()
    hilo2.start()

    # Esperar a que los hilos terminen
    hilo1.join()
    hilo2.join()

    print("Hilos completados")

# Ejecutar la función asíncrona en el bucle principal de asyncio
async def main():
    await asyncio.gather(
        funcion_asincrona(),
        funcion_asincrona()
    )

asyncio.run(main())



import asyncio
import threading
import multiprocessing
import time

# Función del hilo
def tarea_hilo(nombre):
    print(f"Iniciando tarea del hilo: {nombre}")
    time.sleep(2)  # Simular tarea de I/O
    print(f"Tarea del hilo finalizada: {nombre}")

# Función asíncrona para lanzar hilos
async def funcion_asincrona():
    print("Ejecutando función asíncrona")
    hilo1 = threading.Thread(target=tarea_hilo, args=("hilo1",))
    hilo2 = threading.Thread(target=tarea_hilo, args=("hilo2",))

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    print("Hilos completados en función asíncrona")

# Función del proceso
def funcion_proceso():
    asyncio.run(funcion_asincrona())

# Crear procesos y lanzar
if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=funcion_proceso)
    proceso2 = multiprocessing.Process(target=funcion_proceso)

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

import multiprocessing
import time

# Función que se ejecutará en múltiples procesos
def tarea_proceso(nombre):
    print(f"Iniciando el proceso: {nombre}")
    time.sleep(2)  # Simula una tarea intensiva
    print(f"Proceso terminado: {nombre}")

# Ejecutar la función en varios procesos
if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=tarea_proceso, args=("Proceso 1",))
    proceso2 = multiprocessing.Process(target=tarea_proceso, args=("Proceso 2",))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print("Todos los procesos han terminado")
