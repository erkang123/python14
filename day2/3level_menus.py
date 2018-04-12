#Author:Erkang

data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "通天苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{},
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    }
}
flag=False
while not flag:
    for i in data: #显示第一层
        print(i)

    choice = input("请选择进入>>>：") #选择第一层数据
    if choice in data:
        while not flag:
            for i in data[choice]: #显示第二层
                print('\t',i)

            choice2 = input("请选择进入>>>：")#选择第二层数据
            if choice2 in data[choice]:
                while True:
                    for i in data[choice][choice2]:  #显示第三层
                        print('\t\t', i)

                    choice3 = input("请选择进入>>>：")  # 选择第三层数据
                    if choice3 in data[choice][choice2]:
                        while not flag:
                            for i in data[choice][choice2][choice3]:
                                print('\t\t\t', i)

                            choice4=input("最后一层，按B返回>>>：")
                            if choice4 =='B' or choice4 =='b':
                                pass
                            elif choice4 =='q':
                                falg=True
                    if choice3 == 'B' or choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        falg = True
            if choice2 == 'B' or choice2 == 'b':
                break
            elif choice2 == 'q':
                falg = True