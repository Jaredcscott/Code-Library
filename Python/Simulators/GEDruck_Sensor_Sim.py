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
   sckt.bind(('localhost', port))  # Creates the port binding for 127.0.0.1:10102
   sckt.listen()  #Socket object will now listen for activity on the specified port
   sckt.settimeout(3)
   print('Serving GEDRuck Data on at 127.0.0.1:' + str(port) + '\nListening....')
   while True:
      conn = None
      try:
         #Outer try is watching for a keyboard interrupt coming from the inner try when it throws a timeout exception 
         try:
            '''
               KeyboardInterrupt does not reach main call stack until process is complete. 
               The timeout will complete the process and exit with a timeout exception.
               If the user has entered a keyboard interrupt, the timeout will allow that exception to be caught
            '''
            conn, address = sckt.accept()  # Establish connection with client
            print('Incoming connection from address: ', str(address[0]) + ":" + str(address[1]))
            simulateSensor(conn,address)
         except socket.timeout:
            print("Listening....")
            continue
      except KeyboardInterrupt:
         print("Shutting down sensor sim. . .")
         if conn:
            conn.close()
         break      

def genGEDruckData():
   randomValue = random.randint(850,1050)
   dataString = "1: " + str(randomValue) + "\r"
   return dataString

def simulateSensor(sckt):
   #Simulator waits for a 'poll' then sends a data string
   #data = conn.recv(1024)
   #print('Incoming Poll Message:', data.decode())
   dataString = genGEDruckData() #Generating simulated data
   byt = dataString.encode()
   conn.send(byt)

if __name__ == '__main__':
    main()
