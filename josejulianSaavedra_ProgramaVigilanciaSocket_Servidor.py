import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5555)
sock.bind(server_address)

sock.listen(1)


objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']

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
