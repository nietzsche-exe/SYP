import asyncio
import websockets

async def jugar():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Enviar el ID del jugador al servidor
        jugador_id = input("Ingrese su ID de jugador: ")
        await websocket.send(jugador_id)

        while True:
            # Enviar la apuesta al servidor
            apuesta = input("Ingrese su apuesta (del 1 al 20): ")
            await websocket.send(apuesta)

            # Recibir la respuesta del servidor
            respuesta = await websocket.recv()
            print(respuesta)

            if "¡Felicidades!" in respuesta:
                break

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(jugar())