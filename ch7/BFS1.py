from AdjGraph import AdjGraph,INF
from collections import deque
MAXV=100                                #全局变量，表示最多顶点个数
visited=[0]*MAXV
def BFS(G,v):		                    #邻接表G中从顶点v出发的广度优先遍历
    qu=deque()                          #将双端队列作为普通队列qu
    print(v,end=" ")					#访问顶点v
    visited[v]=1						#置已访问标记
    qu.append(v)						#v进队
    while len(qu)>0:                    #队不空循环
        v=qu.popleft()					#出队顶点v
        for j in range(len(G.adjlist[v])):  #处理顶点v的第j个相邻点
            w=G.adjlist[v][j].adjvex        #取第j个相邻顶点w
            if visited[w]==0:			    #若w未访问
                print(w,end=" ")			#访问顶点w
                visited[w]=1				#置已访问标记
                qu.append(w)				#w进队


#主程序
G=AdjGraph()
n,e=6,7
a=[[0,1,1,0,0,0],[0,0,0,0,0,1],  \
	[0,0,0,1,1,1],[0,0,0,0,0,0], \
	[0,0,0,1,0,0],[0,0,0,0,0,0]]
G.CreateAdjGraph(a,n,e)
print("图G")
G.DispAdjGraph()
print("BFS:",end=' ')
BFS(G,0)
