from LinkList import LinkList


def Reverse(L):                 #求解算法
    p=L.head.next			    #p指向首结点
    L.head.next=None		    #将L置为一个空表
    while p!=None:
        q=p.next			    #q临时保存p结点的后继结点
        p.next=L.head.next	    #将p结点插入到表头
        L.head.next=p
        p=q
	

L=LinkList()
a=[1,2,3,4,5]
L.CreateListR(a)
print("L: ",end=''),L.display()
print("逆置")
Reverse(L);
print("L: ",end=''),L.display()

