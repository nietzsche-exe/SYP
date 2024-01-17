import threading

# Variable global para almacenar el texto
texto_global = ""

# Función para escribir el texto en la variable global
def escribir_texto():
    global texto_global
    texto = input("Introduce un texto: ")
    while texto != "-1":
        texto_global += (texto +" ")
        texto = input("Introduce otro texto: ")
    print("Escritura finalizada")

# Función para leer y presentar el texto de la variable global
def leer_texto():
    global texto_global
    print("Leyendo texto...")
    print(texto_global)

# Arrancar el hilo escritor
hilo_escritor = threading.Thread(target=escribir_texto)
hilo_escritor.start()

while True:
    # Esperar a que el hilo escritor termine
    hilo_escritor.join()

    # Arrancar el hilo lector
    hilo_lector = threading.Thread(target=leer_texto)
    hilo_lector.start()

    # Volver a arrancar el hilo escritor
    hilo_escritor = threading.Thread(target=escribir_texto)
    hilo_escritor.start()

    # Si el texto introducido es "-1", salir del bucle
    if texto_global.endswith("-1"):
        break

print("Programa finalizado")
