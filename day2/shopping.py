#Author:Erkang

product_list=[
    ('Iphone6',5800),
    ('Honor',4500),
    ('MacBook',3800),
    ('Coffe',60),
    ('Apple',100),
]
shopping_list=[]
saraly=input('Input your Saraly:')
if saraly.isdigit():  #用户输入数字
    saraly=int(saraly)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice=input('你要买嘛？>>>:')
        if user_choice.isdigit(): #用户选择商品输入数字
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice>=0:#商品存在
                p_item=product_list[user_choice]
                if p_item[1]<=saraly:#买的起
                    shopping_list.append(p_item)
                    saraly-=p_item[1]
                    print('Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m'%(p_item,saraly))
                else:
                    print('你的余额只剩\033[31;1m%s啦，买个毛线啊！\033[0m'%saraly)
            else:
                print('product code [%s] is not code!'%user_choice)
        elif user_choice=='q':
            print('--------shopping list---------')
            for p in shopping_list:
                print(p)
            print('your current balance %s'%saraly)
            exit()
        else:
            print('invalid option!')
else:
    print('输入错误！')