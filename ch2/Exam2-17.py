from CDLinkList import CDLinkList

def Comb(A, B):                     #求解算法
    ta=A.dhead.prior			    #ta指向A的尾结点
    tb=B.dhead.prior			    #tb指向B的尾结点
    ta.next=B.dhead.next			#尾首相连
    B.dhead.next.prior=ta
    tb.next=A.dhead
    A.dhead.prior=tb
    return A

A=CDLinkList()
a=[1,5,3]
A.CreateListR(a)
print("A: ",end=''),A.display()

B=CDLinkList()
b=[2,8,10,20]
B.CreateListR(b)
print("B: ",end=''),B.display()

print("合并为L")
L=Comb(A,B)
print("L: ",end=''),L.display()

