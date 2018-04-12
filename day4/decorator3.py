#Author:Erkang

#嵌套函数

def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()
    print('test')
foo()