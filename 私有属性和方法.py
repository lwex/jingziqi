class Women():
    def __init__(self,name):
        self.name=name
        self.__age=18
    def __secret(self):
        print("%s的名字，%s的岁数"%(self.name,self.__age))
xiaomei=Women("小美")
print(xiaomei._Women__age)
xiaomei._Women__secret()


class Animal():
    def eat(self):
        print("吃")
    def drinl(self):
        print("喝")
class Dog(Animal):
    def play(self):
        print("玩")
    def jiao(self):
        print("汪汪汪")
class Xiaotianquan(Dog):
    def jiao(self):
        print("我会飞")
        super().jiao()
        print("……##……&")
dog=Xiaotianquan()
dog.jiao()
dog.eat()


class A():
    def __init__(self):
        self.name="xm"
        self.__mm="de"
    def xmm(self):
        print("这是一个小秘密%s   %s"%(self.name,self.__mm))
class B(A):
    def fw(self):
        print("")
        self.xmm()
a=A()
a.xmm()
b=B()
print(b.name)
b.fw()
print(a.name)

print(B.__mro__)
