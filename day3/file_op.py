#Author:Erkang

#读
# f = open("C:/Users/Administrator/Desktop/qq号.txt",encoding='utf-8') #文件句柄
# data = f.read()
# print(data)

#写
# f = open("yesterday",'w',encoding='utf-8') #文件句柄
# data = f.write("adfa")

#追加
# f = open("yesterday",'a',encoding='utf-8') #文件句柄
# f.write("\n你好啊")

#循环(low)
# f = open("yesterday",'r',encoding='utf-8') #文件句柄

# for i in range(2):
#     print(f.readline().strip())
# for index,line in enumerate(f.readlines()):
#     if index == 3:
#         print("-------这是啥-----")
#         continue
#     print(line.strip())

#高效循环
# count = 0
# for i in f:
#     if count == 3:
#         print('----------')
#         count+=1
#         continue
#     print(i)
#     count+=1

 #重复读取
f = open("yesterday",'r',encoding='utf-8') #文件句柄
print(f.tell())
print(f.readline().strip())
print(f.readline().strip())
print(f.readline().strip())
print(f.tell())
print('----------')
f.seek(0)
print(f.read())

#实时刷新
f = open("yesterday",'w',encoding='utf-8') #文件句柄
f.write("hello 1 \n")
f.write("hello 1 \n")
f.write("hello 1 \n")
f.flush() #实时从内存缓存刷新到硬盘


f = open("yesterday","r+",encoding='utf-8')#读写
f = open("yesterday","w+",encoding='utf-8')#写读
f = open("yesterday","a+",encoding='utf-8')#追加读写
f = open("yesterday","rb")#二进制文件
f.write("hello world \n".encode())
f.close()