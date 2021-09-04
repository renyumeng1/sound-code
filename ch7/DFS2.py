from MatGraph import MatGraph,INF
MAXV=100                                    #全局变量，表示最多顶点个数
visited=[0]*MAXV
def DFS(g,v):       	                #邻接矩阵g中从顶点v出发的深度优先遍历
    print(v,end=" ")					#访问顶点v
    visited[v]=1					    #置已访问标记
    for w in range(g.n):
        if g.edges[v][w]!=0 and g.edges[v][w]!=INF: 
            if visited[w]==0:		    #存在边<v,w>并且w没有访问过
                DFS(g,w)				#若w顶点未访问,递归访问它

#主程序
g=MatGraph()
n,e=6,7
a=[[0,1,1,0,0,0],[0,0,0,0,0,1],  \
	[0,0,0,1,1,1],[0,0,0,0,0,0], \
	[0,0,0,1,0,0],[0,0,0,0,0,0]]
g.CreateMatGraph(a,n,e)
print("图g")
g.DispMatGraph()
print("DFS",end=' ')
DFS(g,0)
