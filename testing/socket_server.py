import socket
s = socket.socket()
s.bind(('localhost',6969))
s.listen()

conn,addr = s.accept()
print(conn)

data = conn.recv(1024)
print('recv:',data)

conn.send(data.uppper())
s.close()
