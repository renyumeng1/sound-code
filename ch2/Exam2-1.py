from SqList import SqList

def Reverse(L):             #求解算法
    i=0
    j=L.getsize()-1
    while i<j :
        L[i],L[j]=L[j],L[i]
        i+=1
        j-=1

#主程序        
L=SqList()
a=[1,2,3,4,5]
L.CreateList(a)
print("L: ",end=''),L.display()
print("逆置L")
Reverse(L)
print("L: ",end=''),L.display()
