import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print(f"Received from client: {message}")
        response = f"Echo: {message}"
        await websocket.send(response)
        print(f"Sent to client: {response}")

start_server = websockets.serve(handler, '0.0.0.0', 8765)

print("WebSocket server is running...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
