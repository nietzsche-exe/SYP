suma = int(0)
multiplicacion = int(0)
contadorPares = int(0)
contadorImpares = int(0)

for i in range(6):
        numero = int(input('Escribe un numero: '))
        if (numero % 2 == 0):
            contadorPares = contadorPares + 1
            suma += numero
        else:
            contadorImpares = contadorImpares + 1 
            multiplicacion += numero

print('Numero de pares: ' + str(contadorPares) + ', Suma de pares: ' + str(suma))
print('Numero de impares: ' + str(contadorImpares) + ', Multiplicacion de impares: ' + str(multiplicacion))
              
            
            
