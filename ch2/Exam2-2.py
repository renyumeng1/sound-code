from SqList import SqList

def Deletek(L, i, k):                   #求解算法
    assert i>=0 and k>=1 and i+k>=1 and i+k<=L.getsize(),'参数错误'
    for j in range(i+k,L.getsize()):	#将元素前移k个位置
        L[j-k]=L[j]
    L.size-=k			                #长度减k

#主程序        
L=SqList()
a=[1,2,3,4,5]
L.CreateList(a)
print("L: ",end=''),L.display()
i=1
k=3
print("删除L中序号%d开始的%d个元素" %(i,k))
Deletek(L,i,k)
print("L: ",end=''),L.display()
