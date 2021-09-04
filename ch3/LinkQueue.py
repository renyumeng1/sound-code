class LinkNode:                         #链队结点类
    def __init__(self,data=None):       #构造方法
        self.data=data                  #data域
        self.next=None                  #next域
class LinkQueue:      			        #链队类
    def __init__(self):                 #构造方法
        self.front=None                 #队头指针
        self.rear=None                  #队尾指针
    def empty(self):					#判断队是否为空
        return self.front==None
    def push(self,e):			        #元素e进队
        s=LinkNode(e)                   #新建结点s
        if self.empty():				#原链队为空
            self.front=self.rear=s
        else:							#原链队不空
            self.rear.next=s			#将s结点链接到rear结点后面
            self.rear=s
    def pop(self):						#出队操作
        assert not self.empty()			#检测空链队
        if self.front==self.rear:		#原链队只有一个结点
            e=self.front.data			#取首结点值
            self.front=self.rear=None	#置为空队
        else:							#原链队有多个结点
            e=self.front.data			#取首结点值
            self.front=self.front.next	#front指向下一个结点
        return e

    def gethead(self):				    #取队顶元素操作
        assert not self.empty()			#检测空链队
        e=self.front.data			    #取首结点值
        return e


if __name__ == '__main__':
    qu=LinkQueue()
    qu.push(1)
    qu.push(2)
    qu.push(3)
    qu.push(4)
    print("队头元素: %d" %(qu.gethead()))
    print("出队顺序:",end=' ')
    while not qu.empty():
        print(qu.pop(),end=' ')
    print()
    