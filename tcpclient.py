#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8080

clientsocket.connect(("192.168.0.74", port))
message = clientsocket.recv(1024)
clientsocket.close()
print(message.decode("ascii"))
