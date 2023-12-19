import random
import threading

objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']
max_iteraciones = 50
max_vigilancia = 150

personas = 0
vehiculos = 0

def camara():
    global personas, vehiculos
    for _ in range(max_iteraciones):
        obj = random.randint(-10, 4)
        if obj <= 0:
            obj = 0
        objeto_detectado = objetos[obj]
        if objeto_detectado == 'persona':
            personas += 1
        elif objeto_detectado in ['coche', 'moto', 'bicicleta']:
            vehiculos += 1

def vigilanciaPersonas():
    global personas
    for _ in range(max_vigilancia):
        if personas > 0:
            print(f"Soy el hilo 1 y llevo {personas} persona(s).")
        else:
            print("Soy el hilo 1 y no se ha detectado ninguna persona.")
        personas = 0

def vigilanciaVehiculos():
    global vehiculos
    for _ in range(max_vigilancia):
        if vehiculos > 0:
            print(f"Soy el hilo 2 y llevo {vehiculos} vehículo(s).")
        else:
            print("Soy el hilo 2 y no se ha detectado ningún vehículo.")
        vehiculos = 0

# Crear los hilos
camara_hilo = threading.Thread(target=camara)
vigilancia_personas_hilo = threading.Thread(target=vigilanciaPersonas)
vigilancia_vehiculos_hilo = threading.Thread(target=vigilanciaVehiculos)

# Iniciar los hilos
camara_hilo.start()
vigilancia_personas_hilo.start()
vigilancia_vehiculos_hilo.start()

# Esperar a que los hilos terminen
camara_hilo.join()
vigilancia_personas_hilo.join()
vigilancia_vehiculos_hilo.join()
