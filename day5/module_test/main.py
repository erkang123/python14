#Author:Erkang

# import module_alex
#module_alex = all_code  把模块module_alex下的所有代码复制并赋值个变量（即module名）

# from module_alex import say_hello
# from module_alex import *
#
#print(module_alex.name)
#module_alex.say_hello()
#say_hello()
import sys,os
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
import p_test