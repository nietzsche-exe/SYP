import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5555)
sock.bind(server_address)

sock.listen(1)

objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']

async def escucharSocket():
    while True:
        print('Esperando una conexión...')
        connection, client_address = await loop.sock_accept(sock)
        print('Conexión establecida desde', client_address)

        try:
            while True:
                data = await loop.sock_recv(connection, 1024)
                if not data:
                    break
                data_str = data.decode()
                print(f'Se ha detectado un objeto: {data_str}')
                if data_str not in objetos:
                    print("¡Objeto desconocido!")
                    
        finally:
            connection.close()

async def imprimirPorPantalla():
    while True:
        print("este mensaje se imprime cada 5 segundos")
        await asyncio.sleep(5)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # Create tasks
    tasks = [escucharSocket(), imprimirPorPantalla()]
    loop.run_until_complete(asyncio.gather(*tasks))

    
    

    