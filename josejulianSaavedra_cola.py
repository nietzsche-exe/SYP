import queue
import threading

# Crear una cola para almacenar los textos ingresados
cola = queue.Queue()

# Función para el hilo escritor
def escritor():
    while True:
        texto = input("Ingrese un texto: ")
        if texto != "-1":
            cola.put(texto)
        else:
            cola.put("0x01")  # Código de finalización
            break

# Función para el hilo lector
def lector():
    while True:
        elemento = cola.get()
        if elemento != "0x01":
            print(elemento)
        else:
            print(elemento)
            break
        

# Crear y arrancar los hilos
hilo_escritor = threading.Thread(target=escritor)
hilo_lector = threading.Thread(target=lector)

hilo_escritor.start()
hilo_lector.start()
