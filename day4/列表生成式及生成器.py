#Author:Erkang

#列表生成式
[i*2 for i in range(10)]

def func(args):
    print(args)
[func(i) for i in range(10)]

#列表生成器
(i*2 for i in range(10))
