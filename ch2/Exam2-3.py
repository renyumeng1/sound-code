from SqList import SqList

def Deletex1(L, x):                     #求解算法1
    k=0;
    for i in range(L.getsize()):
        if L[i]!=x:			            #将不为x的元素插入到data中
            L[k]=L[i]
            k+=1
    L.size=k                            #重置长度       


def Deletex2(L, x):                     #求解算法2
    k=0;
    for i in range(L.getsize()):
        if L[i]!=x:				        #将不为x的元素前移k个位置
            L[i-k]=L[i]
        else:							#累计删除的元素个数k
            k+=1
    L.size-=k			                #重置长度
        
   

def Deletex3(L, x):                     #求解算法3
    i=-1
    j=0
    while j<L.getsize():				#j遍历所有元素
        if L[j]!=x:				        #找到不为x的元素a[j]
            i+=1					    #扩大不为x的区间
            if i!=j:
                L[i],L[j]=L[j],L[i]     #将data[i]与data[j]交换
        j+=1							#继续扫描
    L.size=i+1						    #重置长度

#主程序
a=[1,2,1,5,1]
L1=SqList()
L1.CreateList(a)
print("L1: ",end=''),L1.display()
x=1
print("解法1:删除L1中所有%d的元素" %(x),end=' ')
Deletex1(L1,x)
print("L1: ",end=''),L1.display()

L2=SqList()
L2.CreateList(a)
print("L2: ",end=''),L2.display()
x=1
print("解法2:删除L2中所有%d的元素" %(x),end=' ')
Deletex2(L2,x)
print("L2: ",end=''),L2.display()

L3=SqList()
L3.CreateList(a)
print("L3: ",end=''),L3.display()
x=1
print("解法3:删除L3中所有%d的元素" %(x),end=' ')
Deletex3(L3,x)
print("L3: ",end=''),L3.display()
