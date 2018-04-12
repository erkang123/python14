#Author:Erkang

info = {
    'stu1101':'TengLan Wu',
    'stu1102':'LongZe Luola',
    'stu1103':'XiaoZe Maliya',
}
print(info)

print(info['stu1101']) #查
print(info.get('stu1101'))#查

info['stu1101']="武藤兰" #改

info['stu1104']="CangJingkong"#增

#del info    #删除整个字典
del info['stu1101']
info.pop('stu1101')
info.popitem()    #随机删除

print('stu1104' in info)#判断字典是否存在这个键  info.has_key('11013') py2.x

print(info)

for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)