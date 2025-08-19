# trying to make a connection to a foreign address

import socket, ssl

hostname = "www.youtube.com"
addr = (hostname, 443)

raw_sock = socket.create_connection(addr)   # TCP connection
context = ssl.create_default_context()      # SSL config
secure_sock = context.wrap_socket(raw_sock, server_hostname=hostname)

req = b"GET / HTTP/1.1\r\nHost: www.youtube.com\r\nConnection: close\r\n\r\n"
secure_sock.sendall(req)

res = secure_sock.recv(4096)
print(res.decode(errors="ignore"))

secure_sock.close()