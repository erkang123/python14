#Author:Erkang

f = open("yesterday",'r',encoding='utf-8')
f_new = open("yesterday.bak",'w',encoding='utf-8')

for line in f:
    if "这都是我的错" in line:
        line = line.replace("这都是我的错","这都bu是我的错")
    f_new.write(line)
