import socket  # Import socket module

port = 10101  # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()  # Create a socket object
host = ""  # Get local machine name
s.bind(('localhost', port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

print('Server listening....')

x = 0

while True:
    conn, address = s.accept()  # Establish connection with client.

    while True:
        try:
            print('Got connection from', address)
            data = conn.recv(1024)
            print('Server received', data)

            st = '1: 995.66<13>'
            byt = st.encode()
            conn.send(byt)

        except Exception as e:
            print(e)
            break

conn.close()