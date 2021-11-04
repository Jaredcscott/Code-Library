'''
    @Author Jared Scott ☯
    This file defines a 'Executor' class which will initiate a listener and maintain a Watcher when needed 
    Acts as a central program file
'''

import websockets
import random
import time
import os
import asyncio
from listener import WS_Listener
from watcher import File_Watcher

class WS_Executor:
    def __init__(self,host,port):
        self._host = host 
        self._port = port
        self.listener = WS_Listener(self._host,self._port)
    
    async def start(self):
        print("Starting a Command Listener on " + str(self._host) + ":" + str(self._port))
        await self.listener.serveSocket()
        watch_file = '<FILE NAME TO WATCH>'
        print("Watching: " + watch_file)
        self.watcher = File_Watcher(watch_file, action, text='yes, changed')  # Call action function when file has been changed
        self.watcher.watch()  # start the watch going
    
    def formatResults(self,results_filepath):
        with open(results_filepath) as file:
            falures = []
            lines = file.readlines()
            for line in lines:
                if line.contains("failure"):
                    #There is a failed test in the results 
                    failures.append(line) 
                else:
                    continue
    
# Call this function each time a change happens
def action(text):
    print(str(text))    
                    
async def main():
    host = "192.168.109.13"
    port = 10321  #Port where this process will "Listen" 
    Executor = WS_Executor(host,port) 
    await Executor.start()   
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())