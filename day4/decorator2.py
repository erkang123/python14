#Author:Erkang
import time

def bar():
    time.sleep(3)
    print('in the bar')
def test1(func): # func = bar
    print('in the test1')
    star_time = time.time()
    func() #run bar()
    current_time=time.time()
    print('the func is run time %s'%(current_time-star_time))
test1(bar)
bar()