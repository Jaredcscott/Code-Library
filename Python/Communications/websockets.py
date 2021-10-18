'''
    @Author Jared Scott 
    This is an example of websocket communication using python. 
'''

import asyncio
import websockets
import json

#Change this path variable to the websocket endpoint desired. 
uri = "ws://<URI PATH>/"   
timeout = 5

async def connectToSocket(uri):
    #Connecting to the socket
    async with websockets.connect(uri) as websocket:
        #Enter the desired request data into this dictionary 
        request = {
            'key':'val'
            }
        print("Sending: "+ request)
        await websocket.send(request)
        # Wait for the message with a timeout
        response =  await asyncio.wait_for(websocket.recv(), timeout)
        print("Response: " + str(response))
    #Closing connection when finished 
    await websocket.close()

if __name__ == "__main__":
	asyncio.get_event_loop().run_until_complete(connectToSocket(uri))
