import websockets
import random
import time
import os
import asyncio

async def main():
    host = "192.168.109.13"
    port = 10321  #Port where this process will "Listen" 
    async with websockets.serve(parseCommand, host, port):
        print("Listening . . .")
        await asyncio.Future()  # run forever        

async def parseCommand(websocket, path):
    timeout = 10
    command = await asyncio.wait_for(websocket.recv(), timeout)
    print('Incoming command: ' + str(command))
    print(command)
    if command.split(":")[0] == "RUN TEST":
        print("Running Test: " + str(command.split(":")[1]))
        await websocket.send("Running Test: " + str(command.split(":")[1]))
        runTest()
    elif command == "TEST":
        await websocket.send("Success, message received at remote machine")
        print("Success, message received")
    else: 
        print("Invalid message received")
    await websocket.close() 
    
def runTest():
    os.system("Test_Complete.bat")
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
