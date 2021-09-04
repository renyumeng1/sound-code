from SqStack import SqStack
def isPalindrome(str):		            #例3.5的算法
    st=SqStack()                        #建立一个顺序栈
    n=len(str)
    i=0
    while i<n//2:						#将str前半字符进栈
        st.push(str[i])
        i+=1							#继续遍历str
    if n%2==1:							#n为奇数时
        i+=1							#跳过中间的字符
    while i<n:							#遍历str的后半字符
        if st.pop()!=str[i]:
            return False				#若str[i]不等于出栈字符返回False
        i+=1
    return True							#是回文返回True
#主程序
print("测试1")
str="abcba"
if isPalindrome(str):
    print(str+"是回文")
else:
    print(str+"不是回文")
print("测试2")
str="1221"
if isPalindrome(str):
    print(str+"是回文")
else:
    print(str+"不是回文")
