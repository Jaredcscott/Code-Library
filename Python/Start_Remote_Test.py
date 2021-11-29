'''
    @Author Jared Scott ☯
    Script uses websockets to connect to a remote server
'''

#import socket  # Import socket module

#socket = socket.socket()  # Create a socket object
#test_host = "192.168.176.54"
#port =  10321 # Remote port which you want to connect with

#socket.connect((test_host, port)) 

#msg = "TEST"
#msg = "RUN TEST:I2-R2-T2"
#byt = msg.encode()
#socket.send(byt)

import asyncio
import websockets

async def hello():
    uri = "ws://192.168.176.54:10321"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Run Test:I2-R5-T7")
        print(f">>> {"Run Test:I2-R5-T7"}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

asyncio.run(hello())
