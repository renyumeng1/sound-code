from MatGraph import MatGraph,INF
from collections import deque
MAXV=100                                #全局变量，表示最多顶点个数
visited=[0]*MAXV
def BFS(g,v):		#邻接矩阵g中从顶点v出发的广度优先遍历
    qu=deque()                          #将双端队列作为普通队列qu
    print(v,end=" ")					#访问顶点v
    visited[v]=1						#置已访问标记
    qu.append(v)						#v进队
    while len(qu)>0:                    #队不空循环
        v=qu.popleft()					#出队顶点v
        for w in range(g.n):
            if g.edges[v][w]!=0 and g.edges[v][w]!=INF:
                if visited[w]==0:		#存在边<v,w>并且w未访问
                    print(w,end=" ")    #访问顶点w
                    visited[w]=1	    #置已访问标记
                    qu.append(w)	    #w进队

#主程序
g=MatGraph()
n,e=6,7
a=[[0,1,1,0,0,0],[0,0,0,0,0,1],  \
	[0,0,0,1,1,1],[0,0,0,0,0,0], \
	[0,0,0,1,0,0],[0,0,0,0,0,0]]
g.CreateMatGraph(a,n,e)
print("图g")
g.DispMatGraph()
print("BFS:",end=' ')
BFS(g,0)
