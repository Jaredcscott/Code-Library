'''
   @Author Jared Scott
   This script will open a socket connection at the specified port number hosted from localhost (127.0.0.1)
   This socket when conntacted will generate a random data value and return this data over the socket.
'''

import socket
import random

def main():
    port = 10170  #Port where the sensor data will be 'Served'
    sckt = socket.socket()
    sckt.bind(('localhost', port))  # Creates the port binding for 127.0.0.1:10150
    sckt.listen()  #Socket object will now listen for activity on the specified port
    print('Server listening....')
    simulateSensor(sckt)

def fillDicts():
    data = {"nearN":0,"nearNE":0,"nearE":0,"nearSE":0,"nearS":0,"nearSW":0,"nearW":0,"nearNW":0,
            "distN":0,"distNE":0,"distE":0,"distSE":0,"distS":0,"distSW":0,"distW":0,"distNW":0,
            "ovhd":0,"cloud":0,"total":0}
    for item in data:
        data[item] = str(random.randint(10000,29999))
    return data

def genVSS928Data(dataDict):
    #See ICD for Vaisala TSS924
    data = dataDict
    dataStringNear = "NEAR: N "+data["nearN"]+" NE "+data["nearNE"]+" E "+data["nearE"] +" SE "+data["nearSE"]+\
                     " S "+data["nearS"]+" SW "+data["nearSW"]+" W "+data["nearW"]+" NW "+data["nearNW"]+"\x0D\x0A"
    dataStringDist = "DIST: N "+data["distN"]+" NE "+data["distNE"]+" E "+data["distE"] +" SE "+data["distSE"]+" S "+\
                     data["distS"]+" SW "+data["distSW"]+" W "+data["distW"]+" NW "+data["distNW"]+"\x0D\x0A"
    dataStringMisc = "OVHD " + data["ovhd"] + " CLOUD " + data["cloud"] + " TOTAL " + data["total"] + " P 00H 20 C 0 0 0 0 0 0.000"

    return dataStringNear + dataStringDist + dataStringMisc

def simulateSensor(sckt):
    dict = fillDicts()
    dataString = genVSS928Data(dict)  # Generating simulated data
    conn, address = sckt.accept()  # Establish connection with client.
    print('Incoming connection from address: ', str(address[0]) + ":" + str(address[1]))
    while True:
        #Simulator waits for a 'poll' then sends a data string
        data = conn.recv(1024)
        print('Incoming Poll Message:', data.decode())
        dataString = genVSS928Data(dict) #Generating simulated data
        byt = dataString.encode()
        conn.send(byt)
    conn.close()

if __name__ == '__main__':
    main()
