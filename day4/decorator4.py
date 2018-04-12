#Author:Erkang
import time
#添加高阶函数添加附加功能  原函数代码未变，但是调用方式已经改变
'''
def deco(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print('%s is fun time %s'%(func,(stop_time-start_time)))
def test1():
    time.sleep(3)
    print('in the test1')

def test2():
    time.sleep(3)
    print('in the test2')

deco(test1)  #test1()
deco(test2)  #test2()
'''

#添加return 但此时未添加附件功能
'''
def deco(func):
    start_time=time.time()
    return func()
    stop_time=time.time()
    print('%s is fun time %s'%(func,(stop_time-start_time)))
def test1():
    time.sleep(3)
    print('in the test1')

def test2():
    time.sleep(3)
    print('in the test2')
test1=deco(test1)
test1()

test2=deco(test2)
test2()
'''
#添加嵌套函数
# def timer(func): # timer(test1)  func = test1
#     def deco():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('%s is fun time \033[41;1m%s\033[0m'%(func,(stop_time-start_time)))
#     return deco
# @timer
# def test1():
#     time.sleep(3)
#     print('in the test1')
#
# def test2():
#     time.sleep(3)
#     print('in the test2')
#
# #下面的注释可以用@timer代替
# '''
# deco=timer(test1) #此时返回deco函数内存地址,deco函数并未执行
# test1=deco #把deco内存地址赋值给test1,已经覆盖了原test1名称
# '''
# test1()#此时调用deco函数

#遇到需要被修饰的函数有参数时
def timer(func): # timer(test1)  func = test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('%s is fun time \033[41;1m%s\033[0m'%(func,(stop_time-start_time)))
    return deco
@timer
def test1():
    time.sleep(3)
    print('in the test1')
@timer
def test2(name,age):
    time.sleep(3)
    print('in the test2')
    print(name,age)

#下面的注释可以用@timer代替
'''
deco=timer(test1) #此时返回deco函数内存地址,deco函数并未执行
test1=deco #把deco内存地址赋值给test1,已经覆盖了原test1名称
'''
test1()#此时调用deco函数
test2('erkang',23)