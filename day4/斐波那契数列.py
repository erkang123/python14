#Author:Erkang

#生成斐波那契数列函数
# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b = b,a+b
#         n+=1
#     return 'done'
# fib(10)
# t=(b,a+b)  t是一个tuple
# a=t[0]
# b=t[1]

#变成生成器
def fib(max):
    n,a,b=0,0,1
    while n<max:
        #print(b)
        yield b
        a,b = b,a+b
        n+=1
    return 'done'

#f=fib(10)
g=fib(6)
while True:
    try:
        x= next(g)
        print('g',x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break
# print(f.__next__())
# print('=========')
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
#
# print('======start loop=====')
# for i in f:
#     print(i)