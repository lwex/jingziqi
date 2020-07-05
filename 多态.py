class Dog():
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s蹦蹦跳跳的玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s飞上天玩耍" % self.name)


class Person():
    def __init__(self, name):
        self.name = name

    def playwithDog(self, dog):
        print("%s和%s开心的玩耍" % (self.name, dog.name))
        dog.game()


xiaomei = Person("小美")
erha = XiaoTianDog("哮天犬")
xiaomei.playwithDog(erha)


class Tool():
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


ft = Tool("斧头")
shuitong = Tool("水桶")
print(Tool.count)
print(shuitong.count)


class Tools():
    counts = 0

    @classmethod
    def showcount(cls):
        print("工具的数量是：%s" % cls.counts)

    def __init__(self, name):
        self.name = name
        Tools.counts += 1


fts = Tools("斧头")
shuitongs = Tools("水桶")
Tools.showcount()
shuitongs.showcount()


class Game():
    best_score = 0

    @staticmethod
    def print_tishi():
        print("游戏操作：让僵尸进来")

    @classmethod
    def print_best_score(cls):
        print("最高分数是：%s" % cls.best_score)

    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s开始游戏！" % self.name)


Game.print_tishi()
Game.print_best_score()
xm = Game("小美")
xm.play()


class MusicPlaier():
    def __new__(cls, *args, **kwargs):
        print("分配音乐播放器")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("这是一个音乐播放器")


musicplay = MusicPlaier()
print(musicplay)

print()


class Danli():
    instant = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instant is None:
            cls.instant = super().__new__(cls)
        return cls.instant

    def __init__(self):
        if Danli.init_flag:
            return
        print("初始化")
        Danli.init_flag = True


aa = Danli()
bb = Danli()
print(aa)
print(bb)
