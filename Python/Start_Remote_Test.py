import socket  # Import socket module

socket = socket.socket()  # Create a socket object
test_host = "192.168.176.54"
port =  10321 # Remote port which you want to connect with

socket.connect((test_host, port)) 

#msg = "TEST"
msg = "RUN TEST:I2-R2-T2"
byt = msg.encode()
socket.send(byt)