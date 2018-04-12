#Author:Erkang
se=input('是否为新用户？Y/N')
count = {}
if se=='Y' or se =='y':
    print('----注册用户----')
    _username=input("Username:")
    _password=input("Password:")
    # count{_username:_password
    f1=open('C:/Users/Administrator/Desktop/老男孩python/user.txt','r+')
    f2 = open('C:/Users/Administrator/Desktop/老男孩python/passwd.txt', 'w')
    if f1.read()==_username:
        print('用户名已存在,请重新输入！')
        _username = input("Username:")
        f1.write(_username)
    else:
        f1.write(_username)
        f1.close()
    f2.write(_password)
    f2.close()
else:
    for i in range(3):
        print('----登录----')
        username=input('Username:')
        password=input('Password:')

        f3=open('C:/Users/Administrator/Desktop/老男孩python/user.txt','r')
        user=f3.read()
        f3.close()

        f4=open('C:/Users/Administrator/Desktop/老男孩python/passwd.txt','r')
        passw=f4.read()
        f4.close()

        if user==username and passw==password:
            print('welcome login...')
            break
        else:
            if user!=username and passw==password:
                print('用户名输入有误')
            elif user==username and passw != password:
                print('密码错误')
            else:
                print('用户名或密码输入错误或不存在')