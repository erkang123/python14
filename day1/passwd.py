#Author:Erkang
import getpass

_username="erkang"
_password="123"
username=input('name:')
# password=getpass.getpass('password')
password=input('password')

if _username==username and _password==password:
    print('welcome user {name} login ...'.format(name=username))
else:
    print('inviled username or password')