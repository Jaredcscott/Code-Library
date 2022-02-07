'''
    @Author Jared Scott ☯
    This file will not work properly until the <XXXX> tags have been replaced with their proper values 
    Example of inter program communication using websockets
'''
import websockets
import random
import time
import os
import asyncio

async def main():
    host = "<Enter Host IP>"
    port = <Enter Service Port>  #Port where this process will "Listen" 
    async with websockets.serve(parseCommand, host, port):
        print("Listening . . .")
        await asyncio.Future()  # run forever        

async def parseCommand(websocket, path):
    timeout = 10
    message = await asyncio.wait_for(websocket.recv(), timeout)
    print('Incoming message: ' + str(message))
    print(message)
    if len(message) > 0:
        print("Message Received: " + str(message))
        await websocket.send("Message Received: " + str(message))
        run()
    else: 
        print("Invalid message received")
    await websocket.close() 
    
def run():
    #Do something interesting
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
