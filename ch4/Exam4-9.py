def disp(A):						#输出二维数组A
    n=len(A)
    for i in range(n):
        for j in range(n):
            print(" %d" %(A[i][j]),end=' ')
        print()

def compression(A,a):		#将A压缩存储到a中
    for i in range(len(A)):
        for j in range(i+1):
            k=i*(i+1)//2+j
            a[k]=A[i][j]
def getk(i,j):						#由i、j求压缩存储中的k下标
    if i>=j:
        return(i*(i+1)//2+j)
    else:
        return(j*(j+1)//2+i)

def Mult(a,b,C,n):	#矩阵乘法
    for i in range(n):
        for j in range(n):
            s=0
            for k in range(n):
                k1=getk(i,k)
                k2=getk(k,j)
                s+=a[k1]*b[k2]
            C[i][j]=s

#主程序
n=3
m=n*(n+1)//2
A=[[1,2,3],[2,4,5],[3,5,6]]
B=[[2,1,3],[1,5,2],[3,2,4]]
C=[[0]*n for i in range(n)]
a=[0]*m
b=[0]*m
print("A:"); disp(A)
print("A压缩存储到a中")
compression(A,a)
print("a:",end=' ')
for i in range(m):
    print(" %d"%(a[i]),end=' ')
print()
print("B:"); disp(B)
print("B压缩存储到b中")
compression(B,b)
print("b:",end=' ')
for i in range(m):
    print(" %d" %(b[i]),end=' ')
print()
print("C=A*B")
Mult(a,b,C,n)
print("C:"); disp(C)	
