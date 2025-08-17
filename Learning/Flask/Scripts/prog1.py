# messing around with socket

# fd = file descriptor, an integer assigned to any I/O object, like an open file or a socket listening at a port

import socket

server = socket.socket() # this opens a socket with IPv4 TCP
print(server.fileno()) # prints the fd of the socket

local_addr = ("localhost", 8080)
print(f"Listening on port 8080.....")

server.bind(local_addr) # binding the socket to an IP and port
server.listen() # listening for connection on the IP and port bound to the socket


conn, addr = server.accept() # if a TCP handshake is initiated the OS will handle it

print(f"Connected to {addr}")
conn.sendall(b"Hello there, from port 8080") # the b"" sends data in byte format

conn.close()
