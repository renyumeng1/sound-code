from AdjGraph import AdjGraph,INF
MAXV=100                                    #全局变量，表示最多顶点个数
visited=[0]*MAXV

def DFS(G,v):	                            #邻接表G中从顶点v出发的深度优先遍历
    print(v,end=' ')			            #访问顶点v
    visited[v]=1							#置已访问标记
    for j in range(len(G.adjlist[v])):      #处理顶点v的所有出边顶点j
        w=G.adjlist[v][j].adjvex            #取顶点v的一个相邻点w
        if visited[w]==0:
            DFS(G,w)						#若w顶点未访问,递归访问它

def DFS1(G,v):	                            #邻接表G中从顶点v出发的深度优先遍历
    print(v,end=' ')			            #访问顶点v
    visited[v]=1							#置已访问标记
    for p in G.adjlist[v]:                  #处理顶点v的所有出边顶点
        w=p.adjvex                          #取顶点v的一个相邻点w
        if visited[w]==0:
            DFS1(G,w)						#若w顶点未访问,递归访问它


#主程序
G=AdjGraph()
n,e=6,7
a=[[0,1,1,0,0,0],[0,0,0,0,0,1],  \
	[0,0,0,1,1,1],[0,0,0,0,0,0], \
	[0,0,0,1,0,0],[0,0,0,0,0,0]]
G.CreateAdjGraph(a,n,e)
print("图G")
G.DispAdjGraph()
print("DFS  ",end=' ')
DFS(G,0)
print()
for i in range(MAXV): visited[i]=0
print("DFS1 ",end=' ')
DFS1(G,0)

