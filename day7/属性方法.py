class Dog(object):
    name = '222'
    def __init__(self,name):
        self.name = name
    #@staticmethod #实际上跟类没什么关系了
    # @classmethod
    @property
    def eat(self):
        print("%s is eating %s"%(self.name,'sdf'))
    @eat.setter
    def eat(self,food):
        print("set food is:",food)

d= Dog("ChenRonghua")
d.eat
d.eat = "ddf"