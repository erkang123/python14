class Role:
    n = 123 #类变量
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #构造函数
        #在实例化时做一些类的初始化的工作
        self.name =name #实例变量(静态属性)，作用域就是实例本身
        self.role =role
        self.weapon = weapon
        self.__life_value =life_value #私有属性
        self.money = money
    def __del__(self):#析构函数
        print("")
    def shot(self):#类的方法，功能（动态属性）
        print("shooting...")