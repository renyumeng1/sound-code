from LinkList import LinkList

def Split(L,A,B):                       #求解算法
    p=L.head.next			            #p指向L的首结点
    t=A.head							#t始终指向A的尾结点
    while p!=None:						#遍历L的所有数据结点
        t.next=p
        t=p							    #尾插法建立A
        p=p.next						#p后移一个结点
        if p!=None:
            q=p.next;					#临时保存p结点的后继结点
            p.next=B.head.next			#头插法建立B
            B.head.next=p
            p=q							#p指向q结点
    t.next=None							#尾结点next置空

#主程序
L=LinkList()
a=[1,2,3,4,5,6]
L.CreateListR(a)
print("L: ",end=''),L.display()
A=LinkList()
B=LinkList()

print("拆分")
Split(L,A,B)
print("A: ",end=''),A.display()
print("B: ",end=''),B.display()

