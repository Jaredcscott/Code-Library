'''
 NOTE: Chrome system variables, make a TLS log
'''

import socket
import random

port = 10150  #Port where the sensor data will be 'Served'
sckt = socket.socket()
sckt.bind(('localhost', port))  # Creates the port binding for 127.0.0.1:10150
sckt.listen()  #Socket object will now listen for activity on the specified port
print('Server listening....')


def genBelfortData():
    randomValue = random.uniform(12,14)
    dataString = "\x01\x02\x0DVP" + str(randomValue)[:5] + "DE4" + "\r\n"
    return dataString

def simulateSensor():
    conn, address = sckt.accept()  # Establish connection with client.
    print('Incoming connection from address: ', str(address[0]) + ":" + str(address[1]))
    while True:
        #Simulator waits for a 'poll' then sends a data string
        data = conn.recv(1024)
        print('Incoming Poll Message:', data.decode())
        dataString = genBelfortData() #Generating simulated data
        byt = dataString.encode()
        conn.send(byt)
    conn.close()

simulateSensor()