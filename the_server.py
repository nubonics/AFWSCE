import asyncio
import sys

import qasync as qasync
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
from hypercorn import Config
from hypercorn.asyncio import serve

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.websocket_route("/ws")
async def websocket(websocket: WebSocket):
    # Accept the clients request for a connection
    await websocket.accept()

    # Get the data sent from the client
    data = await websocket.receive_json()
    print(f'clients message: {data}')

    # Respond to the client
    await websocket.send_json({"msg": "Hello Client"})

    # Cleanup, by closing the websocket
    await websocket.close()


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        print(data)


async def reverse_proxy():
    config = Config()
    config.bind = ["0.0.0.0:10000"]
    # config.certfile = f'{data_directory}/certificates/cert.pem'
    # config.keyfile = f'{data_directory}/certificates/key.pem'
    config.loglevel = 'debug'
    return await serve(app, config)


async def main():
    # Run the server as a task, so that if need-be, we can run other async programs in parallel to this server
    tasks = list()
    tasks.append(asyncio.create_task(reverse_proxy()))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        qasync.run(main())
    except (asyncio.exceptions.CancelledError, RuntimeError):
        sys.exit(0)
