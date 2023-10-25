
import multiprocessing

def escribir_en_fichero(texto, nombre_fichero):
     with open(nombre_fichero, "a") as fichero:
        fichero.write(texto + "\n")

# Función para el proceso lector
def leer_fichero_y_mostrar(nombre_fichero):
    with open(nombre_fichero, 'r') as fichero:  
        contenido = fichero.read()
        print("Contenido del fichero:")
        print(contenido)

if __name__ == "__main__":

    nombre_fichero = "fichero.txt"
    
    while True:
        texto = input("Escribe un texto: (cuando escribas -1 termina el programa)")
    
        if texto == "-1":
            break
        else:
    
            proceso_escritor = multiprocessing.Process(target=escribir_en_fichero, args=(texto, nombre_fichero))
            proceso_escritor.start()
            proceso_escritor.join()
    
            proceso_lector = multiprocessing.Process(target=leer_fichero_y_mostrar, args=(nombre_fichero,))
            proceso_lector.start()
            proceso_lector.join()
    

print("Fin del programa")




 
    
