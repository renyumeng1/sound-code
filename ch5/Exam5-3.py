from LinkList import LinkList
def Positive(p):                #正向输出所有结点值
    if p==None:
        return
    else:
        print("%d" %(p.data),end=' ')
        Positive(p.next)


def Reverse(p):                #反向输出所有结点值
    if p==None:
        return
    else:
        Reverse(p.next)
        print("%d" %(p.data),end=' ')

	
L=LinkList()
a=[1,2,3,4]
L.CreateListR(a)
print("L:",end=' ');L.display()
p=L.head.next
print("正向输出:",end=' ')
Positive(p)
print()
print("反向输出:",end=' ')
Reverse(p)
print()
