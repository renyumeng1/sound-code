from MatGraph import MatGraph,INF,MAXV
from AdjGraph import AdjGraph,ArcNode
import heapq                                #导入优先队列模块
#基本Dijkstra算法
def Dijkstra1(g,v):         	            #求从v到其他顶点的最短路径
    dist=[-1]*MAXV				            #建立dist数组
    path=[-1]*MAXV				            #建立path数组
    S=[0]*MAXV					            #建立S数组
    for i in range(g.n):
        dist[i]=g.edges[v][i]				#最短路径长度初始化
        if g.edges[v][i]<INF:			    #最短路径初始化
            path[i]=v						#v到i有边，置路径上顶点i的前驱为v
        else:								#v到i没边时，置路径上顶点i的前驱为-1
            path[i]=-1
    S[v]=1									#源点v放入S中
    u=-1
    for i in range(g.n-1):				    #循环向S中添加n-1个顶点
        mindis=INF						    #mindis置最小长度初值
        for j in range(g.n):				    #选取不在S中且具有最小距离的顶点u
            if S[j]==0 and dist[j]<mindis: 
                u=j
                mindis=dist[j]
        S[u]=1						        #顶点u加入S中
        for j in range(g.n):					#修改不在s中的顶点的距离
            if S[j]==0:						#仅仅修改S中的顶点j
                if g.edges[u][j]<INF and dist[u]+g.edges[u][j]<dist[j]:
                    dist[j]=dist[u]+g.edges[u][j]
                    path[j]=u
    DispAllPath(dist,path,S,v,g.n)			#输出所有最短路径及长度

def DispAllPath(dist,path,S,v,n):           #输出从顶点v出发的所有最短路径
    for i in range(n):					    #循环输出从顶点v到i的路径
        if S[i]==1 and i!=v:
            apath=[]
            print("  从%d到%d最短路径长度: %d \t路径:" %(v,i,dist[i]),end=' ')
            apath.append(i)				    #添加路径上的终点
            k=path[i];
            if k==-1:						#没有路径的情况
                print("无路径")
            else:							#存在路径时输出该路径
                while k!=v:
                    apath.append(k)		    #顶点k加入到路径中
                    k=path[k]
                apath.append(v)			    #添加路径上的起点
                apath.reverse()             #逆置apath
                print(apath)                #输出最短路径

#改进Dijkstra算法
def Dijkstra2(G,v):                         #改进的狄克斯特拉算法
    dist=[INF]*MAXV				            #建立dist数组,初始化dist[i]为∞
    S=[0]*MAXV					            #建立S数组,初始化S[i]为0
    heap=[]                                 #优先队列元素为[d,i]，按d权值建立小根堆
    for j in range(len(G.adjlist[v])):      #处理顶点v的所有出边
        w=G.adjlist[v][j].adjvex            #取顶点v的第j个邻接点w
        dist[w]=G.adjlist[v][j].weight;		#距离初始化
        heapq.heappush(heap,[dist[w],w])    #将[dist[w],w]进队
    S[v]=1									#源点v添加S中
    for i in range(G.n-1):					#循环直到所有顶点的最短路径都求出
        p=heapq.heappop(heap)			    #出队最小路径长度的结点p
        u=p[1]								#取最小最短路径长度的顶点u
        S[u]=1								#顶点u加入S中
        for j in range(len(G.adjlist[u])):  #处理顶点u的所有出边
            w=G.adjlist[u][j].adjvex        #取顶点u的第j个邻接点w
            if S[w]==0 and dist[u]+G.adjlist[u][j].weight<dist[w]:
                dist[w]=dist[u]+G.adjlist[u][j].weight	#修改最短路径长度
                heapq.heappush(heap,[dist[w],w])        #将[dist[w],w]进队
    print("从%d顶点出发的最短路径长度如下:" %(v))
    for i in range(G.n):							    #输出结果
        if i!=v:
            print("  %d到顶点%d的最短路径长度: %d" %(v,i,dist[i]))

#主程序
g=MatGraph()
n,e=7,12
a=[[0,4,6,6,INF,INF,INF],
	[INF,0,1,INF,7,INF,INF],
	[INF,INF,0,INF,6,4,INF],
	[INF,INF,2,0,INF,5,INF],
	[INF,INF,INF,INF,0,INF,6],
	[INF,INF,INF,INF,1,0,8],
	[INF,INF,INF,INF,INF,INF,0]]       #图7.35的边数组
g.CreateMatGraph(a,n,e)
print("图g")
g.DispMatGraph()
print("Dijkstra1求解结果");
Dijkstra1(g,0)

G=AdjGraph()
G.CreateAdjGraph(a,n,e)
print("图G")
G.DispAdjGraph()
print("Dijkstra2求解结果");
Dijkstra2(G,0)

