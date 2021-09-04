from AdjGraph import AdjGraph,INF

def DeGree1(G,v):	                    #无向图邻接表G中求顶点v的度
	return len(G.adjlist[v])            #顶点v的度为G.adjlist[v]的长度                   

def DeGree2(G,v):    	                #有向图邻接表G中求顶点v的出度和入度
    ans=[0,0]                           #ans[0]累计出度,ans[1]累计入度
    ans[0]=len(G.adjlist[v])            #顶点v的出度为G.adjlist[v]的长度
    for i in range(G.n):			    #遍历所有的头结点
        for p in G.adjlist[i]:
            if p.adjvex==v:             #存在<i,v>的边
                ans[1]+=1               #顶点v的入度增加1
                break
    return ans							#返回出度和入度
   

#主程序
G=AdjGraph()
n,e=5,8
a=[[0,1,0,1,1],[1,0,1,1,0],[0,1,0,1,1],[1,1,1,0,1],[1,0,1,1,0]]
G.CreateAdjGraph(a,n,e)
print("图G1")
G.DispAdjGraph()
print("求解结果");
for i in range(G.n):
    print("  顶点%d的度: %d" %(i,DeGree1(G,i)))

G1=AdjGraph()
n,e=5,8
b=[[0,1,0,1,0],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,0],[1,0,0,1,0]]
G1.CreateAdjGraph(b,n,e)
print("图G2")
G1.DispAdjGraph()
print("求解结果");
for i in range(G1.n):
    ans=DeGree2(G1,i)
    print("  顶点%d的度: %d" %(i,ans[0]+ans[1]))
