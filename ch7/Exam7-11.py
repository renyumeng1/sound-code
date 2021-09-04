from MatGraph import MatGraph,INF,MAXV
A=[[0]*MAXV for i in range(MAXV)]           #全局变量,A数组
pcnt=[[0]*MAXV for i in range(MAXV)]        #全局变量,路径中顶点个数
def Floyd(g):           	                #Floyd算法
    for i in range(g.n):					#数组A和pcnt初始化
        for j in range(g.n): 
            A[i][j]=g.edges[i][j]
            if i!=j and g.edges[i][j]<INF:
                pcnt[i][j]=2;			    #<i,j>作为路径，含2个顶点
            else:	
                pcnt[i][j]=0;			    #没有路径，顶点个数为0
    for k in range(g.n):					#求Ak[i][j]和pcnt[i][j]
        for i in range(g.n):
            for j in range(g.n):
                if A[i][j]>A[i][k]+A[k][j]:
                    A[i][j]=A[i][k]+A[k][j]
                    pcnt[i][j]=pcnt[i][k]+pcnt[k][j]-1;
                    
def Mincycle(g):                    		#找一个最小环长度
    minl=INF
    Floyd(g)
    for i in range(g.n):
        for j in range(g.n):
            if i!=j and A[i][j]<INF and pcnt[i][j]>2 and g.edges[j][i]<INF:
                minl=min(minl,A[i][j]+g.edges[j][i])
    return minl

#主程序
g=MatGraph()
n,e=5,10
a=[	[0,13,INF,4,INF],[13,0,15,INF,5], \
    [INF,INF,0,12,INF],[4,INF,12,0,INF],[INF,INF,6,3,0]]
g.CreateMatGraph(a,n,e)
print("图g")
g.DispMatGraph()
print("最小环长度=%d" %(Mincycle(g)))