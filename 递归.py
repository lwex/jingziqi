def print_num(num):
    print(num)
    if num == 1:
        return
    print_num(num - 1)


print_num(3)

def sum_number(num):
    if num==1:
        return 1
    temp=sum_number(num-1)
    return temp+num
result=sum_number(3)
print(result)
