import socket  # Import socket module
import os
import re


s = socket.socket()  # Create a socket object
port = 10101  # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect(('localhost', port))

# send message for hundred times
while True:
    while True:
        data = s.recv(1024)
        if data:
            print(data)
            x += 1
            break

        else:
            print('no data received')