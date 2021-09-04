class LinkNode:                         #单链表结点类
    def __init__(self,data=None):       #构造方法
        self.data=data                  #data域
        self.next=None                  #next域

class LinkStack:                        #链栈类
    def __init__(self):                 #构造方法
        self.head=LinkNode()            #头结点head
        self.head.next=None

    def empty(self):                    #判断栈是否为空
        if self.head.next==None:
            return True
        return False
        
    def push(self,e):                   #元素e进栈
        p=LinkNode(e)
        p.next=self.head.next
        self.head.next=p

    def pop(self):                      #元素出栈
        assert self.head.next!=None     #检测空栈的异常
        p=self.head.next;
        self.head.next=p.next
        return p.data

    def gettop(self):                     #取栈顶元素
        assert self.head.next!=None         #检测空栈的异常
        return self.head.next.data

if __name__ == '__main__':
    st=LinkStack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print("出栈顺序:",end=' ')
    while not st.empty():
        print(st.pop(),end=' ')
    print()
