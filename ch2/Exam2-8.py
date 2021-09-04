from LinkList import LinkList

def Delmaxnodes(L):                     #求解算法
    p=L.head.next                       #p指向首结点
    maxe=p.data                         #maxe置为首结点值
    while p.next!=None:					#查找最大结点值maxe
        if p.next.data>maxe:
            maxe=p.next.data
        p=p.next
    pre=L.head							#pre指向头结点
    p=pre.next							#p指向pre的后继结点
    while p!=None:						#p遍历所有结点
        if p.data==maxe:				#p结点为最大值结点
            pre.next=p.next				#删除p结点
            p=pre.next					#让p指向pre的后继结点
        else:
            pre=pre.next				#pre后移一个结点
            p=pre.next					#让p指向pre的后继结点
        
L=LinkList()
a=[5,2,1,5,3,5]
L.CreateListR(a)
print("L: ",end=''),L.display()
print("删除所有最大结点")
Delmaxnodes(L);
print("L: ",end=''),L.display()

