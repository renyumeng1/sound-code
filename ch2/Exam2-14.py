from DLinkList import DLinkList

def Swap(L,x):                      #求解算法
    p=L.dhead.next			        #p指向首结点
    q=None;
    while p!=None:                  #查找最后一个值为x的结点q
        if p.data==x:q=p
        p=p.next
    if q==None or L.dhead.next==q:  #不存在x结点或者该结点是首结点
        return                      #直接返回
    else:                           #找到值为x的结点q
        pre=q.prior
        pre.next=q.next             #删除q结点
        if q.next!=None:
            q.next.prior=pre
        pre.prior.next=q            #将q结点插入到pre结点之前
        q.prior=pre.prior
        pre.prior=q;
        q.next=pre

#主程序
L=DLinkList()
a=[1,5,6,3,5,6]
L.CreateListR(a)
print("L: ",end=''),L.display()
x=6
print("x=",x)
print("交换")
Swap(L,x)
print("L: ",end=''),L.display()

