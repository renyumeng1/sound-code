from LinkStack import LinkStack
def Reverse(st):                    #逆置栈st
    a=[]
    while not st.empty():			#将出栈的元素放到列表a中
        a.append(st.pop())
    for j in range(len(a)):         #将列表a的所有元素进栈
        st.push(a[j])
    return st
#主程序
st=LinkStack()
print("1,2,3,4依次进栈")
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print("st逆置->st1")
print("st1出栈序列: ",end=' ')
st1=Reverse(st)
while not st1.empty():
    print(st1.pop(),end=' ')
print()