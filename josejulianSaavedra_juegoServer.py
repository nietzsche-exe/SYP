import asyncio
import websockets
import random

async def juego_adivinanza(websocket, path):
    id_jugador = await websocket.recv()
    print(f"Conexión establecida con el jugador {id_jugador}")

    numero_secreto = random.randint(1, 20)

    while True:
        apuesta = await websocket.recv()
        apuesta = int(apuesta)

        if apuesta == numero_secreto:
            await websocket.send("¡Felicidades! ¡Adivinaste el número!")
            break
        elif apuesta < numero_secreto:
            await websocket.send("El número es mayor. Inténtalo de nuevo.")
        else:
            await websocket.send("El número es menor. Inténtalo de nuevo.")

if __name__ == "__main__":
    start_server = websockets.serve(juego_adivinanza, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    print("Servidor WebSocket iniciado. Esperando conexiones...")
    asyncio.get_event_loop().run_forever()
