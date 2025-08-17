# the program prog3 will talk to

import socket

client = socket.socket()
server_addr = ("localhost", 8080)
self_addr = ("localhost", 5000)

client.bind(self_addr)
client.connect(server_addr)

print("Connection established....")
print("enter 'exit' to exit connection")

while True:
	msg = client.recv(1024).decode()
	print(f'Server:{msg}')
	res = input("You:")

	client.sendall(res.encode())
	if res == 'exit':
		client.close()
		break

