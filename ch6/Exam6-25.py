MAXN=1005                               #最多结点个数
parent=[-1]*MAXN		                #并查集存储结构
rank=[0]*MAXN			                #存储结点的秩
def Init():					            #并查集初始化 
    global n
    global parent
    global rank
    for i in range(1,n+1):
        parent[i]=i
        rank[i]=0
'''
def Find(x:int):				            #并查集中查找x结点的根结点
    global parent
    if x!=parent[x]:
        parent[x]=Find(parent[x])		#路径压缩 
    return parent[x]
'''
def Find(x:int):							#查找x结点的根结点
    rx=x
    while parent[rx]!=rx:					#找到x的根rx
        rx=parent[rx]
    y=x
    while y!=rx:							#路径压缩
        parent[y]=rx
        y=parent[y]
    return rx								#返回根
    
def Union(x:int,y:int):		            #并查集中x和y的两个集合的合并
    global parent
    global rank
    rx=Find(x)
    ry=Find(y)
    if rx==ry:							#x和y属于同一棵树的情况 
        return
    if rank[rx]<rank[ry]:
        parent[rx]=ry					#rx结点作为ry的孩子 
    else:
        if rank[rx]==rank[ry]:			#秩相同，合并后rx的秩增1
            rank[rx]+=1
        parent[ry]=rx					#ry结点作为rx的孩子  

#主程序
while True:                     #循环处理多个测试用例
    tmp=list(map(int,input().split()))
    n=tmp[0]
    if n==0: break;		        #n=0结束
    m=tmp[1]                    #m条道路
    Init()						#初始化
    for i in range(m):			#输入m条边
        tmp=list(map(int,input().split()))
        a=tmp[0]
        b=tmp[1]
        Union(a,b)
    ans=0
    for i in range(1,n+1):	    #求子树个数ans
        if parent[i]==i:
            ans+=1
    print(ans-1)		        #结果为ans-1
