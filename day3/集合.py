#Author:Erkang

list_1 = [1,3,4,5,6,7,9]
list_1 = set(list_1)
print(list_1,type(list_1))

list_2 = set([2,6,0,66,22,8,4])
print(list_2,type(list_2))

#交集
print(list_1.intersection(list_2))

#并集
print(list_1.union(list_2))

#差集 in list_1 but not in list_2
print(list_1.difference(list_2))

#子集
list_3 = set([1,3,7])
print(list_3.issubset(list_1))
print(list_1.issuperset(list_3))

#对称差集  取出两者间不同的数据
print(list_1.symmetric_difference(list_2))

print("--------------")

list_4 = set([5,6,7,8])
#两者之间无相同数据时，返回True
print(list_3.isdisjoint(list_4))

#交集
print (list_1 & list_2)

#union
print (list_1 | list_2)

#different
print(list_1 - list_2)

#对称差集
print(list_1 ^ list_2)

list_1.add(999)
list_1.update([99,88,77]) #同时添加多个数

print(list_1.pop())

list_1.discard(88)