class Foo(object):
    def __init__(self):
        self.name = "erkang"
    def func(self):
        return 'func'
obj = Foo()

#检查是否含有成员
print(hasattr(obj,'name'))
print(hasattr(obj,"func"))

#获取成员
print(getattr(obj,"name"))
print(getattr(obj,'func'))

#设置成员
setattr(obj,'age',18)
setattr(obj,'show',lambda num: num+1)

#删除成员
delattr(obj,'name')
delattr(obj,'func')