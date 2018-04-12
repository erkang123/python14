# class People: #经典类
class People(object):#新式类写法
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def eat(self):
        print("%s is eating..."%self.name)
    def talk(self):
        print("%s is talking..."%self.name)
    def sleep(self):
        print("%s is sleeping..."%self.name)
class Man(People):
    def __init__(self,name,age,money):
        People.__init__(self,name,age)
        super(Man,self).__init__(name,age) #新式类的写法
        self.money =money
        print('')
    def sleep(self):
        People.sleep(self)
        print("man is sleeping....")

class Woman(People):
    def get_birth(self):
        print("%s is born a baby ..." %self.name)
m1 =Man('老牛',22)
m1.eat()
m1.sleep()

w1 =Woman("老杨",28)
w1.get_birth()