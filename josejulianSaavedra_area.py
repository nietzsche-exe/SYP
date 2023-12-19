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

