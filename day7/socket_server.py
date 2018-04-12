import socket
import os
server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听的端口
server.listen() #监听
while True:
    print('我要开始等电话了')
    conn,addr = server.accept() #等电话打进来
    #conn就是客户端连过来而在服务端为其生成的一个连接实例
    print(conn,addr)
    print('电话来了')
    while True:
        data = conn.recv(1024)
        print('recv:', data)
        if not data:
            break
        # conn.send(data.upper())
        # res = os.popen(data).read()
        # conn.send(res)
        # conn.sendall(res)
        f = open('视频文件')
        data = f.read()
        conn.send(data)

server.close()