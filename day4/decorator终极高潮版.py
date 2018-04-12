import time

# user,passwd='erkang','123'
# def auth(func):
#     def wrapper(*args,**kwargs):
#         username = input('Username:').strip()
#         password = input('Password:').strip()
#         if user == username and passwd== password:
#             print("\033[32;1m User has passed authentiction\033[0m")
#             func(*args,**kwargs)
#         else:
#             exit("\033[31;1mInvalid username or password\033[0m")
#     return wrapper
#
# def index():
#     print('welcome to index page')
# @auth
# def home():
#     print('welcome to home page')
# @auth
# def bbs():
#     print('welcome to bbs page')
#
# index()
# home()
# bbs()

#被装饰的函数添加return的结果
# user,passwd='erkang','123'
# def auth(func):
#     def wrapper(*args,**kwargs):
#         username = input('Username:').strip()
#         password = input('Password:').strip()
#         if user == username and passwd== password:
#             print("\033[32;1m User has passed authentiction\033[0m")
#             return func(*args,**kwargs)
#         else:
#             exit("\033[31;1mInvalid username or password\033[0m")
#     return wrapper
#
# def index():
#     print('welcome to index page')
# @auth
# def home():
#     print('welcome to home page')
#     return "from home"
# @auth
# def bbs():
#     print('welcome to bbs page')
#
# index()
# print(home())
# bbs()


# 不同函数使用不同的装饰方法
user,passwd='erkang','123'
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type=='local':
                username = input('Username:').strip()
                password = input('Password:').strip()
                if user == username and passwd == password:
                    print("\033[32;1m User has passed authentiction\033[0m")
                    return func(*args, **kwargs)
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            else:
                print('搞毛线ldap,不会。。。')
        return wrapper
    return out_wrapper
def index():
    print('welcome to index page')
@auth(auth_type='local')  #home = wrapper()
def home():
    print('welcome to home page')
    return "from home"
@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()