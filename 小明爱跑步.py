class Person():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("%s重%s公斤" % (self.name, self.weight))

    def __str__(self, ):
        return "%s爱跑步%s公斤" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("我要减肥")

    def eat(self):
        self.weight += 1
        print("吃完这顿再减")


xiaoming = Person("xiaoming", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)


class Item():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s的占地面积为%s" % (self.name, self.area)


class Home():
    def __init__(self, hx, mj):
        self.hx = hx
        self.mj = mj
        self.free_mj = mj
        self.jj_list = []

    def __str__(self):
        return ("户型：%s\n面积：%0.2f\n剩余面积：%0.2f\n家具：%s"
                % (self.hx, self.mj, self.free_mj, self.jj_list))

    def add_item(self, item):
        print("要添加%s" % item)
        if item.area <= self.free_mj:
            self.free_mj -= item.area
            self.jj_list.append(item.name)
        else:
            print("%s面积太大，无法添加" % item.name)


ximengsi = Item("席梦思", 40)
guizi = Item("柜子", 20)
yizi = Item("椅子", 1.5)

print(ximengsi)
my_home = Home("两室一厅", 60)
print(my_home)
my_home.add_item(ximengsi)
my_home.add_item(guizi)
my_home.add_item(yizi)
print(my_home)


class Gun():
    def __init__(self, xh):
        self.xh = xh
        self.zd_count = 0

    def zhuangq(self, shuliang):
        self.zd_count += shuliang

    def fire(self):
        if self.zd_count <= 0:
            print("%s没有子弹啦！！快跑！！！" % self.xh)
            return
        self.zd_count -= 1
        print("%s开火，突突突[剩余：%s]" % (self.xh, self.zd_count))


class Solder():
    def __init__(self, name):
        self.name = name
        self.qiang = None

    def kqq(self):
        if self.qiang == None:
            print("你还没有枪呀")
            return
        print("开枪啊！[%s]" % self.name)
        self.qiang.fire()
# def creat_user():
#     print("请输入用户名：")
#     a=input()
#     b=Solder(a)
#     print(b)
#     print("选择下一步：0.开枪 1.装子弹")
#     n=input()
#     if b.qiang==None:
#         print("请输入添加您的武器：")
#         wq=input()
#         nd_wq=Gun(wq)
#         b.qiang=nd_wq
#     if n==0:
#         b.kqq()
#         if b.qiang.zd_count==0:
#             print("请添加子弹！输入子弹个数：")
#             gs=input()
#             b.qiang.zhuangq(gs)
#         b.kqq()
#     if n==1:
#         print("请添加子弹！输入子弹个数：")
#         gs = input()
#         b.qiang.zhuangq(gs)
#
# creat_user()


ak47 = Gun("ak47")
ak47.zhuangq(30)
xsd = Solder("小恩旭")
xsd.kqq()
xsd.qiang = ak47
xsd.kqq()
mn35 = Gun("mn35")
dbz = Solder("小饼饼")
dbz.qiang = mn35
dbz.kqq()
