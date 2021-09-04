from SqList import SqList

def Middle(A,B):                                #求解算法 
    i=j=k=0
    while i<A.getsize() and j<B.getsize():		#两个有序顺序表均没有扫描完
        k+=1							        #元素比较次数增1
        if A[i]<B[j]:                           #A中当前元素为较小的元素
            if k==A.getsize():					#恰好比较了n次
                return A[i]				        #返回A中的当前元素
            i+=1
        else: 									#B中当前元素为较小的元素
            if k==B.getsize():					#恰好比较了n次
                return B[j]			            #返回B中的当前元素
            j+=1 

A=SqList()
a=[11,13,15,17,19]
A.CreateList(a)
print("A: ",end=''),A.display()
B=SqList()
b=[2,4,6,8,20]
B.CreateList(b)
print("B: ",end=''),B.display()

print("求中位数")
print("结果: %d " %(Middle(A,B)))
