import socket
import random
import time
import os

def main():
    while True:
        port = 10321  #Port where this process will "Listen" 
        sckt = socket.socket()
        sckt.bind(('192.168.176.54', port))  # Creates the port binding for 192.168.176.54:10321
        sckt.listen()  #Socket object will now listen for activity on the specified port
        print('Listening....')
        conn, address = sckt.accept()  # Established connection with remote machine
        print('Incoming message from address: ', str(address[0]) + ":" + str(address[1]))
        data = conn.recv(1024)
        message = data.decode()
        print('Incoming Message:', message)
        
        if message.split(":")[0] == "RUN TEST":
            print("Running Test: " + str(message.split(":")[1]))
            runTest()
            continue
        elif message == "TEST":
            print("Success, message received")
            continue
        else: 
            print("Invalid message received")
            conn.close()
            break

def runTest():
    os.system("Test_Complete.bat")
    
if __name__ == "__main__":
    main()