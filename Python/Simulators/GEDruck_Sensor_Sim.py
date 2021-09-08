import socket
import random
import time

port = 10102  #Port where the sensor data will be 'Served'
sckt = socket.socket()
sckt.bind(('localhost', port))  # Creates the port binding for 127.0.0.1:10150
sckt.listen()  #Socket object will now listen for activity on the specified port
print('Server listening....')


def genGEDruckData():
    randomValue = random.randint(850,1050)
    dataString = "1: " + str(randomValue) + "\r"
    return dataString

def simulateSensor():
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

simulateSensor()