import random

#lista con 20 numeros aleatorios
list = [random.randint(0,100) for _ in range (20)]
print(list)

#Cantidad de numeros en la lista
print(len(list))

#Media de los numeros
print(sum(list)/len(list))

#Insertar la cadena "hola" en la posicion 5
list.insert(4, "Hola")
print(list)

#Sublista con los elementos desde la posicion 6 a la 12
sublist1 = list[6:12] 
print(sublist1)

#Sublista con los 4 ultimos elementos
sublist2 = list[len(list)-4:]
print(sublist2)