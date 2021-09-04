MAXV=100							    #表示最多顶点个数
INF=0x3f3f3f3f				            #表示∞
class ArcNode:                          #边结点
    def __init__(self,adjv,w):          #构造方法
        self.adjvex=adjv                #邻接点
        self.weight=w                   #边的权值

class AdjGraph:				            #图邻接表类
    def __init__(self,n=0,e=0):         #构造方法
        self.adjlist=[]		            #邻接表数组
        self.vexs=[]			        #存放顶点信息，暂时未用
        self.n=n                        #顶点数
        self.e=e			            #边数
    def CreateAdjGraph(self,a,n,e):  	##通过数组a、n和e建立图的邻接表
        self.n=n                        #置顶点数和边数
        self.e=e
        for i in range(n):				#检查边数组a中每个元素
            adi=[]                      #存放顶点i的邻接点
            for j in range(n):
                if a[i][j]!=0 and a[i][j]!=INF: #存在一条边
                    p=ArcNode(j,a[i][j])        #创建<j,a[i][j]>出边的结点p
                    adi.append(p)               #将结点p添加到adi中
            self.adjlist.append(adi)
    def DispAdjGraph(self):				        #输出图的邻接表
        for i in range(self.n):                 #遍历每一个顶点i
            print("  [%d]" %(i),end='')
            for p in self.adjlist[i]:
                print("->(%d,%d)" %(p.adjvex,p.weight),end='')
            print("->∧")
if __name__ == '__main__':
    G=AdjGraph()
    n,e=5,5
    a=[ [0,8,INF,5,INF],
        [INF,0,3,INF,INF],
		[INF,INF,0,INF,6],
        [INF,INF,9,0,INF],
        [INF,INF,INF,INF,0]]
    G.CreateAdjGraph(a,n,e)
    G.DispAdjGraph()
