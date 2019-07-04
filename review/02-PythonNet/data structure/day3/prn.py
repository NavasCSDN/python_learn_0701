"""
逆波兰表达式简单练习
"""

from day3.lstack import *

st = LStack()

while True:
    exp = input("dc:")
    tmp = exp.split(' ')

    for i in tmp:
        if i == 'p':
            break

        if i not in ['+', '-']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)

    print("结果:", st.pop())  # 打印结果
    st.clear() #　将栈清空
