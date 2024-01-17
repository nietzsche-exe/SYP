
import threading

# Creamos la variable global y el objeto Lock
texto_global = ""
lock = threading.Lock()

# Definimos la función que escribirá el texto en la variable global
def escritor(texto):
    global texto_global
    with lock:
        texto_global += (texto+" ")

# Definimos la función que leerá la variable global y la imprimirá en pantalla
def lector():
    global texto_global
    with lock:
        print(texto_global)

# Pedimos el texto por consola y entramos en el ciclo
texto = input("Introduce un texto: ")
while texto != "-1":
    # Creamos el hilo escritor y lo iniciamos
    hilo_escritor = threading.Thread(target=escritor, args=(texto,))
    hilo_escritor.start()

    # Esperamos a que el hilo escritor termine antes de crear el hilo lector
    hilo_escritor.join()

    # Creamos el hilo lector y lo iniciamos
    hilo_lector = threading.Thread(target=lector)
    hilo_lector.start()

    # Pedimos el siguiente texto por consola
    texto = input("Introduce un texto: ")
