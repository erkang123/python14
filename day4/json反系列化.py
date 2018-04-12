#Author:Erkang
import  json
import pickle  #处理复杂的数据
#系列化：把内存里的数据存储在硬盘
# with open('test.text','r') as f:
#     data = eval(f.read())  #eval函数把字符串变成字典
#     print(data)
#     print(type(data))

with open('test.text','r') as f:
    data = json.loads(f.read())
    print(data['name'])