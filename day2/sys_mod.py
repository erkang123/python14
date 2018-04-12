#Author:Erkang

# import sys
# print(sys.path)
# print(sys.argv)
# print(sys.version)

# import os
# # cmd_res=os.system("dir")
# cmd_res=os.popen("dir").read()
# print("-->",cmd_res)
# os.mkdir("new_dir")

msg='我爱北京天安门'
print(msg.encode('utf-8'))
print((msg.encode()).decode())