student = [{"name": "小美"}, {"name": "阿土"}]  # 多个字典放在一个列表中在进行遍历
find_name = "小美"
for student_find in student:
    if student_find["name"] == find_name:
        print("找到了%s" % find_name)
        break
else:
    print("没有找到%s" % find_name)
print("程序结束")

name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[1])
print(name_list.index("wangwu"))
name_list[1] = "李四"
name_list.append("小美眉")
name_list.insert(1, "沙师弟")
example_list = ["孙悟空", "朱二哥"]
name_list.extend(example_list)
name_list.extend(example_list)
name_list.remove("wangwu")
name_list.pop(0)
name_list.pop()
del name_list[0]
# name_list.clear()
list_len = len(name_list)
print("有%d个元素" % list_len)
name_count = name_list.count("孙悟空")
print("sun chuxianle %d ci" % name_count)
print(name_list)
