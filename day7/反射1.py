def bulk(self):
    print("%s is yelling..."%self.name)
class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s is eating..."%self.name)

d = Dog("NiuHanYang")
choice = input('>>:').strip()

# print(hasattr(d,choice))
# print(getattr(d,choice)())

if hasattr(d,choice):
    # func = getattr(d,choice)
    # func()
    delattr(d,choice)
else:
    setattr(d,choice,bulk)
    d.talk(d)

d.name