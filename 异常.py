# try:
#     print("请输入一个整数：")
#     result=8/int(input())
#     print(result)
# except ZeroDivisionError:
#     print("输入不能为0")
# except Exception as result:
#     print("输入错误")
# else:
#     print("尝试成功")
# finally:
#     print("无论成功都执行")
# print("-"*20)


# def demo1():
#     print(int(input("请输入一个整数：")))
# def demo2():
#     return demo1()
# try:
#     demo2()
# except Exception as result:
#     print("未知错误%s"%result)


def password():
    print("请输入密码")
    passwords=input()
    if len(passwords)>=8:
        print("输入正确")
        return passwords
    ex=Exception("密码长度不够")
    raise ex
try :
    print(password())
except Exception as result:
    print(result)