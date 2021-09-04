#顺序栈
class SqStack:
    def __init__(self):             #构造函数
        self.data=[]                #存放栈中元素，初始为空

    def empty(self):                #判断栈是否为空
        if len(self.data)==0:
            return True
        return False

    def push(self,e):               #元素e进栈
        self.data.append(e)

    def pop(self):                  #元素出栈
        assert not self.empty()     #检测栈为空
        return self.data.pop()

    def gettop(self):               #取栈顶元素
        assert not self.empty()     #检测栈为空
        return self.data[len(self.data)-1]

if __name__ == '__main__':
    st=SqStack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print("出栈顺序:",end=' ')
    while not st.empty():
        print(st.pop(),end=' ')
    print()
