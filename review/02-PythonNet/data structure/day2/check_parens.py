from sstack import *

text = '''Both of ((these issues)are (fixed) by postponing the evaluation of annotations. {Instead (of) compiling} code which executes [expressions in] annotations at their definition time, {the compiler} stores the annotation in a string form (equivalent to the [AST of] the) expression in question. 
'''
parens = "()[]{}"  # 验证的括号
left_parens = "([{"
opposite = {')':'(', ']':'[', '}':'{'}  #对应关系

def parent(text):
    #　i记录字符串索引
    i,text_len = 0,len(text)
    while True:
        #　逐个遍历字符串，如果没到结尾并且不是括号就向后遍历
        while i < text_len and text[i] not in parens:
            i += 1

        if i >= text_len:
            return
        else:
            yield text[i],i  #生成括号字符和对应位置
            i += 1


st = SStack()  #　初始化一个栈
for pr,i in parent(text):
    if pr in left_parens:
        st.push((pr,i))  #　将左括号及其位置入栈
    elif st.is_empty() or st.pop()[0] != opposite[pr]:
        print("Unmatching is found at %d for %s"%(i,pr))
        break
else:
    #　循环正常结束，判断栈是否为空
    if st.is_empty():
        print("All parentheses are matched")
    else:
        #　有左括号没有匹配
        e = st.pop()
        print("Unmatching is found at %d for %s"%(e[1],e[0]))















