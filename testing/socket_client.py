import socket
s = socket.socket()
s.connect(('localhost',6969))
s.send(b'wos')

data = s.recv(1024)
print(data)
s.close()