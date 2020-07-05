def demo():
    """zhehijyidh"""
    print("hans")


print(dir(demo))
print(demo.__doc__)


class Cat:

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("cat have to drink")


tom = Cat()
tom.name = "Tom"
tom.drink()
tom.eat()
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
print(tom)
print(lazy_cat)
print(Cat)


class Cats():
    def __init__(self, name):
        print("初始化方法%s" % name)
        self.name = name

    def __del__(self):
        print("wo qu le%s" % self.name)
    def __str__(self):
        return "woshixiaomao%s"%self.name


toms = Cats("hkugi")
print(toms)
print("-"*50)
