from LinkList import LinkList

def Middle1(L):                 #求解算法1
    j=1
    n=L.getsize();
    p=L.head.next;			    #p指向首结点
    while j<=(n-1)//2:			#找中间位置的p结点
        j+=1
        p=p.next;
    return p.data
        
def Middle2(L):                 #求解算法2
    slow=L.head.next
    fast=L.head.next			#均指向首结点
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next			#慢指针每次后移1个结点
        fast=fast.next.next		#快指针每次后移2个结点
    return slow.data
        
        
L=LinkList()
a=[1,2,3,4,5]
L.CreateListR(a)
print("L: ",end=''),L.display()
print("方法1:中位数=%d" %(Middle1(L)))
print("方法2:中位数=%d" %(Middle2(L)))
