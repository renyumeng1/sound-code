class DLinkNode:                            #双链表结点类
    def __init__(self,data=None):           #构造函数
        self.data=data                      #data域
        self.next=None                      #next域
        self.prior=None                     #prior域

class DLinkList:                            #双链表类
    def __init__(self):                     #构造函数
        self.dhead=DLinkNode()              #头结点dhead
        self.dhead.next=None
        self.dhead.prior=None

    def CreateListF(self, a):			    #头插法：由数组a整体建立双链表
        for i in range(0,len(a)):           #循环建立数据结点s
            s=DLinkNode(a[i])				#新建存放a[i]元素的结点s，将其插入到表头
            s.next=self.dhead.next			#修改s结点的next成员
            if self.dhead.next!=None:		#修改头结点的非空后继结点的prior
                self.dhead.next.prior=s
            self.dhead.next=s				#修改头结点的next
            s.prior=self.dhead				#修改s结点的prior

    def CreateListR(self, a):		        #尾插法：由数组a整体建立双链表
        t=self.dhead					    #t始终指向尾结点,开始时指向头结点
        for i in range(0,len(a)):           #循环建立数据结点s
            s=DLinkNode(a[i])			    #新建存放a[i]元素的结点s
            t.next=s					    #将s结点插入t结点之后
            s.prior=t
            t=s
        t.next=None							#将尾结点的next成员置为None


    def geti(self, i):		                #返回序号为i的结点
        p=self.dhead
        j=-1
        while (j<i and p is not None):
            j+=1
            p=p.next
        return p

    def Add(self, e):						    #在线性表的末尾添加一个元素e
        s=DLinkNode(e)		                    #新建结点s
        p=self.dhead
        while p.next is not None:				#查找尾结点p
            p=p.next
        p.next=s;								#在尾结点之后插入结点s
        s.prior=p

    def getsize(self):                          #返回长度
        p=self.dhead
        cnt=0
        while p.next is not None:				#找到尾结点为止
            cnt+=1
            p=p.next
        return cnt
    
    def __getitem__(self,i):                    #求序号为i的元素
        assert i>=0                             #检测参数i正确性的断言
        p=self.geti(i)
        assert p is not None                    #p不为空的检测       
        return p.data

    def __setitem__(self, i, x):                #设置序号为i的元素
        assert i>=0                             #检测参数i正确性的断言
        p=self.geti(i)
        assert p is not None                    #p不为空的检测
        p.data=x

    def GetNo(self,e):							#查找第一个为e的元素的序号
        j=0
        p=self.dhead.next	
        while p is not None and p.data!=e:
            j+=1							    #查找元素e
            p=p.next
        if p is None:
            return -1						    #未找到时返回-1
        else:
            return j							#找到后返回其序号

    def Insert(self, i, e):					    #在线性表中序号i位置插入元素e
        assert i>=0                             #检测参数i正确性的断言
        s=DLinkNode(e)		                    #建立新结点s
        p=self.geti(i-1)				        #找到序号为i-1的结点p
        assert p is not None                    #p不为空的检测       
        s.next=p.next							#修改s结点的next字段
        if p.next!=None:						#修改p结点的非空后继结点的prior字段
            p.next.prior=s
        p.next=s								#修改p结点的next字段
        s.prior=p								#修改s结点的prior字段


    def Delete(self,i): 						#在线性表中删除序号i位置的元素
        assert i>=0							    #检测参数i正确性的断言
        p=self.geti(i)					        #找到序号为i的结点p
        assert p is not None                    #p不为空的检测       
        p.prior.next=p.next					    #修改p结点的前驱结点的next
        if p.next!=None:					    #修改p结点非空后继结点的prior
            p.next.prior=p.prior


    def display(self):					        #输出线性表
        p=self.dhead.next
        while p is not None:
            print(p.data,end=' ')
            p=p.next;
        print()

if __name__ == '__main__':
    L=DLinkList()
    a=[1,2,3,4,1]
    L.CreateListF(a)
    print("L: ",end=''),L.display()
    i=4
    x=10
    print("在序号%d处插入%d" %(i,x))
    L.Insert(i,x)
    print("L: ",end=''),L.display()
    i=4
    print("删除序号%d处元素" %(i))
    L.Delete(i)
    print("L: ",end=''),L.display()

    x=20
    print("添加%d元素" %(x))
    L.Add(x)
    print("L: ",end=''),L.display()

    print("元素1的序号是%d" %(L.GetNo(1)))
    print("L: ",end=''),L.display()


