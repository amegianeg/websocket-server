#!/usr/bin/env python

# WS client example

import asyncio
import uuid

import websockets

TOKEN = "eyJraWQiOiJGQjR2TEMxanhlXC9WQjJcL0lpOTRncTFzMTdYVHc3UTVodElQNklGRFg1TjQ9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJjOGMxM2Q2Yi0xZGVjLTQ3NzktYTEyYy1kYmY3OTE1YzczNGUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfdHBlOGNMV2F3IiwiY29nbml0bzp1c2VybmFtZSI6ImM4YzEzZDZiLTFkZWMtNDc3OS1hMTJjLWRiZjc5MTVjNzM0ZSIsImdpdmVuX25hbWUiOiJBZG1pbiIsImF1ZCI6IjI3dm9sMmNlZ2g5Nm5vYmRsMWcxZGxsMWNtIiwiZXZlbnRfaWQiOiJkYzU1OWYwYi04Njg4LTQ3YjUtODdjZC0wODYxNjZlNDhiMzQiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTU5MzcwMTEyNCwiZXhwIjoxNTkzNzA0NzI0LCJpYXQiOjE1OTM3MDExMjQsImZhbWlseV9uYW1lIjoiSW1lcml0IiwiZW1haWwiOiJhZG1pbkBpbWVyaXQuY29tIn0.RmzsGo2mLFvnNnWm6SQ5KCh1JdPG4OEkAruk5Tqamt2nuSr6y9R0xMu8sqox4hM-BPyPgtnYkzHo_ga7FxT_sxpWgh-ErigpA5cWezZfceAUkQoh7xP3OOUzM45nKhy7kFocH-TDbe5n6cwP0vILo__J7GQWbk6cSZVFS1GAz_sHxzQ_fw01AJcPc9f4BBFtW2ztJKnjeZT8rujNoigbM744cVAQ4Tu6e1sD4ZJ5yplyMXJM8KEw6oH_48TtgORoJAbbcZdEU2t9SWuVmQyBdVc2R1-wTvpp2eaSFL9j9TkV1nMUVUcENUyhDDjsk9Npq6hdqTFrCACMcgIiOZ5-Xw"


async def hello():
    uri = f"ws://localhost:8888/socket.io/?token={TOKEN}"
    async with websockets.connect(uri) as websocket:
        for i in range(20):
            random_string = str(uuid.uuid4())
            await websocket.send(random_string)
            print(f"> {random_string}")

            response = await websocket.recv()
            print(f"< {response}")

asyncio.get_event_loop().run_until_complete(hello())
