<<<<<<< HEAD

import threading

def area_triangulo(base, altura, total):
    area = (base * altura) / 2
    total.append(area)

def area_rectangulo(base, altura, total):
    area = base * altura
    total.append(area)
    
total = []

hilo_triangulo_1 = threading.Thread(target=area_triangulo, args=(10, 12, total))
hilo_triangulo_2 = threading.Thread(target=area_triangulo, args=(2, 5, total))
hilo_rectangulo1 = threading.Thread(target=area_rectangulo, args=(8, 7, total))
hilo_rectangulo2 = threading.Thread(target=area_rectangulo, args=(14, 5, total))

hilo_triangulo_1.start()
hilo_triangulo_2.start()
hilo_rectangulo1.start()
hilo_rectangulo2.start()

hilo_triangulo_1.join()  
hilo_triangulo_2.join()
hilo_rectangulo1.join()
hilo_rectangulo2.join()


area_total = sum(total)
print("El área total es:", area_total)
=======
import threading

area = threading.local()
area.name = "figura irregular"


# Métodos para calcular areas de triangulos, rectangulos y cuadrados
def calcular_area_triangulo(lado1, lado2):
    area_triangulo1 = lado1 * lado2 / 2
    area.value += area_triangulo1
    print(f"El área del triangulo1 es: {area_triangulo1}")
    
def calcular_area_cuadrado(lado):
    area_cuadrado = lado * lado
    area.value += area_cuadrado
    print(f"El área del cuadrado es: {area_cuadrado}")
    
def calcular_area_rectangulo(lado1, lado2):
    area_rectangulo = lado1 * lado2
    area.value += area_rectangulo
    print(f"El área del rectángulo es: {area_rectangulo}")
    
    
# Crear los hilos
t1 = threading.Thread(target=calcular_area_triangulo, args=(10, 12))
t2 = threading.Thread(target=calcular_area_triangulo, args=(2, 5))
t3 = threading.Thread(target=calcular_area_cuadrado, args=(8,))
t4 = threading.Thread(target=calcular_area_rectangulo, args=(5, 14))

t1.start()
t2.start()
t3.start()
t4.start()

# Imprimir el valor final de area.value
print(f"El valor final de la {area.name} es: {area.value}")

>>>>>>> c00eb395f8be092c07f0497b3ecf8adb42afaf5e
