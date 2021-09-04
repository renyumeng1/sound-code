from LinkList import LinkList

def Maxcount(L):                    #求解算法
    cnt=1
    p=L.head.next;			        #p指向首结点
    maxe=p.data					    #maxe置为首结点值
    while p.next!=None:				#循环到p结点为尾结点
        if p.next.data>maxe:		#找到更大的结点
            maxe=p.next.data
            cnt=1
        elif p.next.data==maxe:	    #p结点为当前最大值结点
            cnt+=1
        p=p.next
    return cnt
        
L=LinkList()
a=[2,1,5,3,5]
L.CreateListR(a)
print("L: ",end=''),L.display()
print("最大结点个数=%d" %(Maxcount(L)))
