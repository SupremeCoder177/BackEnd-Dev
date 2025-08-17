# messing around with ports and sockets

import socket

client = socket.socket()

server_addr = ("localhost", 8080)

client.connect(server_addr)
print(client.recv(1024))
client.close()