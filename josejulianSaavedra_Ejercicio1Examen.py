import subprocess
import time
from multiprocessing import Process

def abrirNotePad():
    subprocess.Popen(['notepad.exe','fichero.txt'])

def buscarPalabra():
    while True:
        time.sleep(5)  # Esperar 5 segundos antes de buscar la palabra
        with open('fichero.txt', 'r') as file:
            content = file.read()
            if 'adios' in content:
                print('Se encontró la palabra "adios" en el archivo.')
            else:
                print('No se encontró la palabra "adios" en el archivo.')

if __name__ == '__main__':
    proceso1 = Process(target=abrirNotePad)
    proceso2 = Process(target=buscarPalabra)
    
    proceso1.start()
    proceso2.start()
    
    proceso1.join()
    proceso2.join()
