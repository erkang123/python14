#Author:Erkang

# names="ZhangYang Guyun Xiangpeng XuLiangChen"
names=["ZhangYang","Guyun", "Xiangpeng","XuLiangChen"]

#列表增加
# names.append("ErKang")
# names.insert(1,"Chenronghua")


#改
# names[2]="XuFei"
# print(names)

#delete

# names.remove("Chenronghua")
# del names[1] #= names.pop()
# names.pop()#默认删除最后一个


#列表查询
# print(names[0],names[2])
# print(names[0:3])#切片
# print(names[:3])#切片
# print(names[-2:-1])#切片
# print(names[-2:])#切片

#查找所在位置
print(names)
# print(names.index("Xiangpeng"))
# print( names[names.index("Xiangpeng")] )

#names.clear() #清除列表
# print(names.count("ZhangYang")) #元素计数
# names.reverse()  #反转
# names.sort() #排序

names2=[1,2,3,4]
names.extend(names2)
del names2  #删除变量
print(names)

