
def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

while True:
    anio1 = input("Introduce el primer año: ")
    if anio1.lower() == "end" or anio1.lower() == "fin":
        break
    anio2 = input("Introduce el segundo año: ")
    if anio2.lower() == "end" or anio2.lower() == "fin":
        break

    anio1 = int(anio1)
    anio2 = int(anio2)

    bisiestos = []
    for anio in range(anio1, anio2+1):
        if es_bisiesto(anio):
            bisiestos.append(anio)

    print("Años bisiestos en el intervalo:")
    for anio in bisiestos:
        print(anio)
