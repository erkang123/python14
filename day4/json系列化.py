#Author:Erkang
import  json
#系列化：把内存里的数据存储在硬盘

info = {
    'name':'erkang',
    'age':22,
    'sex':'nan'
}
# with open('test.text','w') as f:
#     info= str(info)
#     f.write(info)

with open('test.text','w') as f:
    data=json.dumps(info)
    f.write(data)