import shelve
import datetime
d = shelve.open("shelve_test") #打开一个文件

# info = {'age':22,'job':'it'}
#
# name = ['alex','rain','test']
# d['name'] = name  #持久化列表
# d['info'] = info  #持久化dict
# d['date'] = datetime.datetime.now()

# print(d.get('name'))
# print(d.get('info'))
# print(d.get('date'))

print(d.items())
for k,v in d.items():
    print(k,v)