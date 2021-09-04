from CLinkList import CLinkList

def Count(L, x):                #求解算法
    cnt=0;						#cnt置为0
    p=L.head.next;			    #首先p指向首结点
    while p!=L.head:			#遍历循环单链表
        if p.data==x:
            cnt+=1				#找到一个值为x的结点cnt增1
        p=p.next				#p后移一个结点
    return cnt

L=CLinkList()
a=[1,5,3,5,6]
L.CreateListR(a)
print("L: ",end=''),L.display()

x=5
print("%d结点的个数=%d" %(x,Count(L,x)))

