N=15
a=[[0]*N for i in range(N)]         #存放螺旋矩阵
def Spiral(x,y,start,n):            #递归创建螺旋矩阵
    if n<=0: return					#递归结束条件
    if n==1:						#矩阵大小为1时
        a[x][y]=start
        return
    for j in range(x,x+n-1):		#上一行
        a[y][j]=start
        start+=1
    for i in range(y,y+n-1):		#右一列
        a[i][x+n-1]=start
        start+=1
    for  j in range(x+n-1,x,-1):	#下一行
        a[y+n-1][j]=start
        start+=1
    for i in range(y+n-1,y,-1):		#左一列
        a[i][x]=start
        start+=1
    Spiral(x+1,y+1,start,n-2)		#递归调用

#主程序
n=4
Spiral(0,0,1,n)
for i in range(0,n):
    for j in range(0,n):
        print("%3d" %(a[i][j]),end=' ')
    print()
