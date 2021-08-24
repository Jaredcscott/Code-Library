import socket  # Import socket module
import random

port = 10150  # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()  # Create a socket object
host = ""  # Get local machine name
s.bind(('localhost', port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

'''
 Chrome system variables, make a TLS log 
'''
print('Server listening....')

SENSOR_CONFIG = "Belfort 6200"


def getBelfortData():
    randomValue = random.randint(10, 14)
    randomMantissa = random.randint(25, 68)
    st = "\x01\x02\x0DVP" + str(float(str(randomValue) + "." + str(randomMantissa))) + "DE4" + "\r\n"
    return st

def simulateSensor(sensor):
    conn, address = s.accept()  # Establish connection with client.
    print('Incoming connection from address: ', str(address[0]) + ":" + str(address[1]))
    while True:
        data = conn.recv(1024)
        print('Incoming Message:', data.decode())
        st = getBelfortData()
        byt = st.encode()
        conn.send(byt)
    conn.close()


simulateSensor(SENSOR_CONFIG)