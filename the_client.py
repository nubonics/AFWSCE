import asyncio
import json
import websockets


async def hello():
    uri = "ws://localhost:10000/ws"
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        send_data_to_the_server = json.dumps({'status': 'hello server'})
        await websocket.send(send_data_to_the_server)

        # Get the response from the server [this implies that there is an expectation of a response]
        # This will fail & crash the program if the server does not send a response back
        greeting = await websocket.recv()
        print(f"servers response: {greeting}")


if __name__ == '__main__':
    asyncio.run(hello())
