from MatGraph import MatGraph,INF

def Degree1(g,v):	                    #无向图邻接矩阵中求顶点v的度
    d=0
    for j in range(g.n):                #统计第v行的非0非∞元素个数
        if g.edges[v][j]!=0 and g.edges[v][j]!=INF:
            d+=1
    return d

def Degree2(g,v): 	                    #有向图邻接矩阵中求顶点v的出度和入度
    ans=[0,0]                           #ans[0]累计出度,ans[1]累计入度
    for j in range(g.n):        	    #统计第v行的非0非∞元素个数为出度
        if g.edges[v][j]!=0 and g.edges[v][j]!=INF:
            ans[0]+=1
    for i in range(g.n):             	#统计第v列的非0非∞元素个数为入度
        if g.edges[i][v]!=0 and g.edges[i][v]!=INF:
            ans[1]+=1
    return ans						    #返回出度和入度

#主程序
g=MatGraph()
n,e=5,8
a=[[0,1,0,1,1],[1,0,1,1,0],[0,1,0,1,1],[1,1,1,0,1],[1,0,1,1,0]]
g.CreateMatGraph(a,n,e)
print("图G1")
g.DispMatGraph()
print("求解结果");
for i in range(g.n):
    print("  顶点%d的度: %d" %(i,Degree1(g,i)))

g1=MatGraph()
n,e=5,8
b=[[0,1,0,1,0],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,0],[1,0,0,1,0]]
g1.CreateMatGraph(b,n,e)
print("图G2")
g1.DispMatGraph()
print("求解结果");
for i in range(g1.n):
    ans=Degree2(g1,i)
    print("  顶点%d的度: %d" %(i,ans[0]+ans[1]))
