'''
   @Author Jared Scott
   This script will open a socket connection at the specified port number hosted from localhost (127.0.0.1)
   This socket when conntacted will generate a random data value and return this data over the socket.
'''

import socket
import random
import time

def main():
    port = 10102  #Port where the sensor data will be 'Served'
    sckt = socket.socket()
    sckt.bind(('localhost', port))  # Creates the port binding for 127.0.0.1:10150
    sckt.listen()  #Socket object will now listen for activity on the specified port
    print('Server listening....')
    simulateSensor(sckt)

def genGEDruckData():
    randomValue = random.randint(850,1050)
    dataString = "1: " + str(randomValue) + "\r"
    return dataString

def simulateSensor(sckt):
    conn, address = sckt.accept()  # Establish connection with client.
    print('Incoming connection from address: ', str(address[0]) + ":" + str(address[1]))
    while True:
        #Simulator waits for a 'poll' then sends a data string
        #data = conn.recv(1024)
        #print('Incoming Poll Message:', data.decode())
        dataString = genGEDruckData() #Generating simulated data
        byt = dataString.encode()
        conn.send(byt)
        time.sleep(10)
    conn.close()

if __name__ == '__main__':
    main()
