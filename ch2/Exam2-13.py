from DLinkList import DLinkList

def Delx(L,x):                          #求解算法
    p=L.dhead.next			            #p指向首结点
    while p!=None and p.data!=x:		#查找第一个值为x的结点p
        p=p.next
    if p!=None:							#找到值为x的结点p
        if p.next!=None:
            p.next.prior=p.prior 		#删除p结点
        p.prior.next=p.next

#主程序
L=DLinkList()
a=[1,5,3,5,6,5]
L.CreateListR(a)
print("L: ",end=''),L.display()
x=5
print("x=",x)
print("删除第一个%d结点" %(x))
Delx(L,x)
print("L: ",end=''),L.display()

