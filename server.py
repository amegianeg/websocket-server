#!/usr/bin/env python

import asyncio
from urllib.parse import urlparse, parse_qs

import websockets


def log(message):
    print(f"[websocket-server] {message}")


async def echo(websocket, path):
    # Log some useful info and retrieve query parameter 'token'
    log(f"Path: {websocket.path}")
    log(f"Request headers: {websocket.request_headers}")
    query_dict = parse_qs(urlparse(path).query)
    token = query_dict.get('token', [''])[0]
    log(f"Token: {token}")

    async for message in websocket:
        log(f"Received: {message}")
        await websocket.send(f"This is the server replying: {message}")

log("Starting server at 0.0.0.0:8088...")
start_server = websockets.serve(echo, "0.0.0.0", 8088)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
