server_list=[]
with open('haproxy','r') as f:
    for line in f:
        if 'backend www.oldboy.org'.strip() in line:
            server=f.read()
            server_list=server_list.append(server)
            print(server_list)