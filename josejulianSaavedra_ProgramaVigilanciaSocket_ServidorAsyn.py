import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.200.169', 5555)
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
                data = await loop.sock_recv(connection, 1024).decode()
                if not data:
                    break
                print(f'Se ha detectado un objeto: {data}')
                    
        finally:
            connection.close()

async def imprimirPorPantalla():
    while True:
        print(".")
        await asyncio.sleep(5)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # Create tasks
    task1 = loop.create_task(escucharSocket())
    task2 = loop.create_task(imprimirPorPantalla())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
