import socket  # Import socket module
import random

port = 10101  # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()  # Create a socket object
host = ""  # Get local machine name
s.bind(('localhost', port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

print('Server listening....')


def getGEDruckData():
    randomValue = random.randint(850, 1050)
    st = "1: " + str(randomValue) + "\r"
    return st


def simulateSensor():
    conn, address = s.accept()  # Establish connection with client.
    print('Incoming connection from address: ', str(address[0]) + ":" + str(address[1]))
    while True:
        data = conn.recv(1024)
        print('Server received', data)
        try:
            st = getGEDruckData()
            byt = st.encode()
            conn.send(byt)
            break

        except Exception as e:
            print(e)
            break

while True:
    simulateSensor()
conn.close()
