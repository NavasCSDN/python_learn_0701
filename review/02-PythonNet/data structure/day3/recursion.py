#　求ｎ的阶乘
def recursion(n):
    #　终止条件
    if n <= 1:
        return 1
    return (n * recursion(n - 1))

r = recursion(5)
print("5！= %d"%r)