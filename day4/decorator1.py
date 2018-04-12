#Author:Erkang
#函数即变量

#示范1
# def foo():
#     print('in the foo')
# foo()

#示范二：
def bar():
    print('in the bar')
def foo():
    print('in the foo')
    bar()
foo()

#示范三：
def foo():
    print('in the foo')
    bar()
def bar():
    print('in the bar')
foo()

#示范四：
# def foo():
#     print('in the foo')
#     bar()
#foo()
# def bar():
#     print('in the bar')