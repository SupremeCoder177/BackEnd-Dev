# Simulating a chat in socket

import socket

addr = ("localhost", 8080)
server = socket.socket()

server.bind(addr) # this binds the socket to the address
server.listen()

con, addr = server.accept() # listens for TCP connections	
print(f"Talking with {addr}")

while True:
	user_msg = input("You:")
	con.sendall(user_msg.encode())
			
	res = con.recv(1024).decode()
	print(f'Client:{res}')

	if res == 'exit':
		con.close()
		break
		