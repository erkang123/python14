#Author:Erkang

name='my name is erkang'
name1='my name is {name} and my years old is {old}'
# print(name.capitalize())
# print(name.count('a'))
# print(name.endswith('ang'))#判断这个字符串以什么结尾
# print(name.center(40,'-'))#打印40个字符，不够的-补齐
# print(name1.format(name='erkang',old=23))
# print('A123abc'.isalnum()) #判断是否是阿拉伯字符
# print('ABCDE'.isalpha())#判断是否是纯英文
# print('123'.isdecimal())#判断是否是十进制
# print('123'.isdigit())#判断是否是纯数字
# print('_abc'.isidentifier())#判断是否是一个合法的标识符(合法变量名)
# print('_abc'.istitle())#判断是否是一个标题
# print('_abc'.islower())#判断是否为小写
# print('_abc'.isupper())#判断是否为大写
# print('+'.join(['1','2','3']))#
# print(name.rjust(50,'*'))#输入50个字符，不够的在右边添加*
# print(name.ljust(50,'*'))#输入50个字符，不够的在左边添加*
# print('erkang'.lower())#字符串变为小写
# print('erkang'.upper())#字符串变为大写
# print('\nerkang'.lstrip())#取消左边换行
# print('erkang\n'.rstrip())#取消右边换行
# print('\nerkang\n'.strip())#取消换行

p=str.maketrans('zxcvbnm','1234567')
print('erkang he'.translate(p))

print('alex li'.replace('l','L',1))
print('alex li'.rfind('1'))
print('alex li'.split('  '))




