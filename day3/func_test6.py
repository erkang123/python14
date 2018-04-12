#Author:Erkang

#*args:接收N个位置参数，转换成元祖形式
def test(*args):
    print(args)
test(3,1)

#**kwargs:把N个关键字参数，转换成字典的方式
def test(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])
test(name='erkang',age=23,sex='n')

def test2(name ,**kwargs):
    print(name)
    print(kwargs)
test2('erkang',age=2,sex='m')

def test3(name ,age=18,**kwargs):
    print(name)
    print(kwargs)
test3('erkang',age=2,sex='m')

def test4(name ,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
test3('erkang',sex='m')