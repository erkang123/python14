#Author:Erkang
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func()
        current_time=time.time()
        print('func is time %s'%(current_time-start_time))
    return wrapper

@timer
def test1():
    time.sleep(3)
    print('in the test1')

test1()