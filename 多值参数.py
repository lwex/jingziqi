# 多值参数
def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(1, 2, 3, 45, name="xiaoming", age=18)


# 多值参数拆包
def demo1(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3, 4)
gl_dict = {"name1": "xiaoming", "age": 18}
demo1(*gl_nums, **gl_dict)
