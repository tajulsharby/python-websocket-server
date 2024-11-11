import asyncio
import websockets

async def handler(websocket, path):
    print(f"New connection from {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            response = f"Echo: {message}"
            await websocket.send(response)
            print(f"Sent to client: {response}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

start_server = websockets.serve(handler, '0.0.0.0', 8765, origins=None)

print("WebSocket server is running...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
