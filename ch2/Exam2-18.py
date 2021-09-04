from CDLinkList import CDLinkList

def Symm(L):                #求解算法
    flag=True;			    #flag表示L是否对称，初始时为真
    p=L.dhead.next;		    #p指向首结点
    q=L.dhead.prior;	    #q指向尾结点
    while flag:
        if p.data!=q.data:  #对应结点值不相同，置flag为假
            flag=False
        else:
            if p==q or p==q.prior: break
            q=q.prior	    #q前移一个结点 
            p=p.next	    #p后移一个结点
    return flag

L=CDLinkList()
a=[1,2,2,1]
L.CreateListR(a)
print("L: ",end=''),L.display()
if Symm(L):
    print("L是对称的")
else:
    print("L不是对称的")
