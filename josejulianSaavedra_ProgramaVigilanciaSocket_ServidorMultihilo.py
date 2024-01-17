import socket
import time
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.200.169', 5555)
sock.bind(server_address)

sock.listen(1)


objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']

def escucharSocket():
    try:
        while True:
            
            print('Esperando una conexión...')
            connection, client_address = sock.accept()
            print('Conexión establecida desde', client_address)

            try:
                while True:
                    
                    data = connection.recv(1024).decode()
                    if not data:
                        break
                    print(f'Se ha detectado un objeto: {data}')
                    
            finally:
                connection.close()
    finally:
        sock.close()
        
def imprimirPorPantalla():
    while True:
        print(".")
        time.sleep(5)


if __name__ == "__main__":
    # Create threads
    task1 = threading.Thread(target=escucharSocket)
    task2 = threading.Thread(target=imprimirPorPantalla)

    # Start threads
    task1.start()
    task2.start()

    # Wait for threads to finish
    task1.join()
    task2.join()

    