from SqList import SqList

def Merge2(A, B):                           #求解算法
    C=SqList()                              #新建顺序表C
    i=j=0                                   #i用于遍历A,j用于遍历B
    while i<A.getsize() and j<B.getsize():  #两个表均没有遍历完毕
        if A[i]<B[j]:
            C.Add(A[i])                     #将较小的A中元素添加到C中
            i+=1
        else:
            C.Add(B[j])                     #将较小的B中元素添加到C中
            j+=1
    while i<A.getsize():					#若A没有遍历完毕
        C.Add(A[i])
        i+=1
    while j<B.getsize():					#若B没有遍历完毕
        C.Add(B[j])
        j+=1
    return C                                #返回C

A=SqList()
a=[1,2,5,8]
A.CreateList(a)
print("A: ",end=''),A.display()
B=SqList()
b=[2,3,4,8,10,15]
B.CreateList(b)
print("B: ",end=''),B.display()

print("合并A和B得到C")
C=Merge2(A,B)
print("C: ",end=''),C.display()
