from LinkList import LinkList
from LinkList import LinkNode

def Commnodes(A,B):                 #求解算法
    p=A.head.next			        #p指向A的首结点
    q=B.head.next			        #q指向B的首结点
    C=LinkList();                   #新建立单链表C
    t=C.head				        #t为C的尾结点
    while p!=None and q!=None:	    #两个单链表都没有遍历完
        if p.data<q.data:		    #跳过较小的p结点
            p=p.next
        elif q.data<p.data:			#将较小结点q链接到C的末尾
            q=q.next
        else:						#p结点和q结点值相同
            s=LinkNode(p.data)      #新建s结点
            t.next=s
            t=s					    #将s结点链接到C的末尾
            p=p.next
            q=q.next
    t.next=None					    #尾结点next置空
    return C

A=LinkList()
a=[1,2,3,5,6]
A.CreateListR(a)
print("A: ",end=''),A.display()

B=LinkList()
b=[2,4,5,6,8,10]
B.CreateListR(b)
print("B: ",end=''),B.display()

print("公共结果")
L=Commnodes(A,B)
print("L: ",end=''),L.display()

