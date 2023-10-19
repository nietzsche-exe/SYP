
#Pedimos el grado de la matriz
n = input("inserte el grado de la matriz")
n = int(n)

#Creamos la matriz identidad de grado n
matriz_identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

#Pintamos la matriz
for matriz in matriz_identidad:
    print(matriz)