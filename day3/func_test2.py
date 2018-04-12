#Author:Erkang
import time

def loger():
    time_format = '%Y-%m-%d %X'
    current_time = time.strftime(time_format)
    with open("log.txt",'a+',encoding='utf-8') as f:
        f.write('\tend action\n')
        f.write(current_time)
def test1():
    print('in the test1')
    loger()
def test2():
    print('in the test2')
    loger()
def test3():
    print('in the test3')
    loger()

test1()
test2()
test3()