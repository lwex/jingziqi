def sayhello():
    print("hello")

if __name__=="__main__":
    print("这是小明设计的模块")
    print(__name__)
    sayhello()
import os
print(os.getcwd())
print(os.listdir())
print(os.listdir("."))
print(os.path.isdir("venv"))
print(os.path.isdir("hanshu.py"))

input_str=input("请输入计算式：")
print(eval(input_str))