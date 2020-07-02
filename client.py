#!/usr/bin/env python

# WS client example

import asyncio
import os
import pathlib
import ssl
import uuid

import websockets

JWT_TOKEN = "FILL ME"
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
localhost_pem = pathlib.Path(os.path.join(os.path.dirname(__file__), "nginx/ssl/cert.pem"))
ssl_context.load_verify_locations(localhost_pem)


async def hello():
    uri = f"wss://localhost:8888/socket.io/?token={JWT_TOKEN}"
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        for i in range(20):
            random_string = str(uuid.uuid4())
            await websocket.send(random_string)
            print(f"> {random_string}")

            response = await websocket.recv()
            print(f"< {response}")

asyncio.get_event_loop().run_until_complete(hello())
