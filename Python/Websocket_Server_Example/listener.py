'''
    @Author Jared Scott
    This file defines a class which will listen on a specific local port using the Websocket protocol
    When a communication is initiated using the websocket, the function 'parseCommand' will be run
'''
import websockets
import random
import time
import os
import asyncio

class WS_Listener:
    def __init__(self,host,port):
        self._host = host 
        self._port = port 
        
    async def serveSocket(self):
        # Starting the Websocket and listening for incoming connections, serving the function 'parseCommand' 
        async with websockets.serve(self.parseCommand, self._host, self._port):
            print("Listening . . .")
            await asyncio.Future()  # run forever      
            
    async def parseCommand(self, websocket):
        timeout = 10
        command = await asyncio.wait_for(websocket.recv(), timeout) #Await a connection with a timeout 
        print('Incoming command: ' + str(command))                  #Command received beginning parsing  
        if command.split(":")[0] == "RUN TEST":                 
            test_name = str(command.split(":")[1])
            print("Running Test: " + test_name)
            self.runTest(test_name)                                 #Valid command received running test process 
            await websocket.send("Test: " + test_name + " Running on " + str(self._host))
            print("Listening . . .")
        elif command == "TEST":
            await websocket.send("Test Successful: Listener is responsive" )
            print("Success, message received")
        else: 
            print("Invalid message received")
        await websocket.close()                                     #Closing communications 
 
    def runTest(self,test_name):
        #This function can be used to perform different actions based on the received command 
        if test_name == 'I2-R3':
            #Runs the Test Automation demo 
            os.system(".\Scripts\I2-R3.bat")
        elif test_name == 'I2-R4':
            #Runs the test cycle I2-R4
            os.system(".\Scripts\I2_R4.bat")
        elif test_name == 'I2-R5':
            #Runs the test cycle I2-R5
            os.system(".\Scripts\I2_R5.bat")
        else: 
            print(test_name + " not found.\nSee C:\\<SCRIPTS LOCATION>\\")
        #pass
