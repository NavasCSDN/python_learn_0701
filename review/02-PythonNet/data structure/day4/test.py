
#　运算此时为　n
#　时间复杂度 　O(n)
def fun(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

# 运算次数　3次
# 时间复杂度　O(1)
def fun1(n):
    sum = (1 + n) * n / 2
    return sum

#　运算次数　n^2 + n
#　时间复杂度　O(n^2)
#　l = [[1,2,3],[4,5,6],[7,8,9]]
def fun2(l):
    for i in l:
        for j in i:
            print(j,end=' ')
        print()



