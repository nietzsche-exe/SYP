
import threading

texto = ""
semaphore = threading.Semaphore()

def escritor(text):
    global texto
    semaphore.acquire()
    texto += (text+" ")
    semaphore.release()

def lector():
    global texto
    semaphore.acquire()
    print(texto)
    texto = ""
    semaphore.release()

while True:
    entrada = input("Introduce un texto: ")
    if entrada == "-1":
        break
    escritor_thread = threading.Thread(target=escritor, args=(entrada,))
    lector_thread = threading.Thread(target=lector)
    escritor_thread.start()
    escritor_thread.join()
    lector_thread.start()
    lector_thread.join()
