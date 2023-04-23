#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())

print(host)
port = 8080

serversocket.bind((host, port))

serversocket.listen(20)

while True:
    clientsocket, address = serversocket.accept()
    print("received connection from: %s " % str(address))
    message = "Get the fuck outta here" + "\r\n"

    clientsocket.send(message.encode("ascii"))
    clientsocket.close()