row = 1
# 星星
while row <= 5:
    print("*" * row)
    row += 1
# 嵌套星星
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1
# 乘法表
m=1
while m<=9:
    n=1
    while n<=m:
        print("%d*%d=%d"%(n,m,m*n),end="\t")
        n+=1
    print("")
    m+=1
