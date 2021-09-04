from SqStack import SqStack
def isMatch(str):			            #判断算法
    st=SqStack()	                    #建立一个顺序栈
    i=0
    while i<len(str):
        e=str[i]
        if e=='(' or e=='[' or e=='{':
            st.push(e)					#将左括号进栈
        else:
            if e==')':
                if st.empty() or st.gettop()!='(':
                    return False          #栈空或栈顶不是'('返回假
                st.pop()
            if e==']':
                if st.empty() or st.gettop()!='[':
                    return False		#栈空或栈顶不是'['返回假
                st.pop()
            if e=='}':
                if st.empty() or st.gettop()!='{':
                    return False;		#栈空或栈顶不是'{'返回假
                st.pop()
        i+=1						    #继续遍历str
    return st.empty()
#主程序
print("测试1")
str="([)]"
if isMatch(str):
    print(str+"中括号是匹配的")
else:
    print(str+"中括号不匹配")
print("测试2")
str="([])"
if isMatch(str):
    print(str+"中括号是匹配的")
else:
    print(str+"中括号不匹配")
