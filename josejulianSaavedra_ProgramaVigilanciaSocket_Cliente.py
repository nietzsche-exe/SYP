import random
import socket
import time

obj = random.randint(-10, 4)
if obj <= 0:
    obj = 0

objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']

server_address = ('localhost', 5555)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(server_address)

for _ in range(10): 
    
    obj = random.randint(1, 4)
    objetoDetectado = objetos[obj]
    sock.send(objetoDetectado.encode())
    time.sleep(1)
    
sock.close()



