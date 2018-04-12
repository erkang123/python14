import socket
client = socket.socket() #声明socket类型，同时生产socket连接对象
client.connect(('localhost',6969))

f = open("视频文件.avi", 'wb')

while True:
    msg = input('>>:').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))    #不能send空，空的话就会卡住
    data = client.recv(102400)
    # print('recv:',data.decode())
    # print(data.decode())
    # f = open("视频文件.avi",'wb')
    f.write(data)

client.close()