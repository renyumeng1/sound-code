class IdxType:								#索引表类型
    def __init__(self,j=None,k=None):       #构造方法
        self.key=k							#关键字（这里是对应块中的最大关键字）
        self.link=j						    #该索引块在数据表中的起始下标

def CreateI(R,I,b):                 		#构造索引表I[0..b-1]
    n=len(R)
    s=(n+b-1)//b;							#每块的元素个数
    j=0
    jmax=R[j]
    for i in range(b):						#构造b个块
        I[i]=IdxType(j)
        while j<=(i+1)*s-1 and j<=n-1:		#j遍历一个块,查找其中最大关键字jmax
            if R[j]>jmax: jmax=R[j]
            j+=1
        I[i].key=jmax
        if j<=n-1:							#j没有遍历完,jmax置为下一个块首元素关键字
            jmax=R[j]

def BlkSearch(R,I,b,k):                 	#在R[0..n-1]和索引表I[0..b-1]中查找k
    n=len(R)
    low,high=0,b-1
    while low<=high:					    #在索引表中折半查找,找到块号为high+1
        mid=(low+high)//2
        if k<=I[mid].key: high=mid-1
        else: low=mid+1
    if high+1>=b: return -1					#块号超界,查找失败,返回-1
    i=I[high+1].link						#求所在块的起始位置
    s=(n+b-1)/b							    #求每块的元素个数s
    if i==b-1:								#第i块是最后块,元素个数可能少于s
        s=n-s*(b-1)
    while i<=I[high+1].link+s-1 and R[i]!=k:
        i+=1
    if i<=I[high+1].link+s-1: return i		#查找成功,返回该元素的序号
    else: return -1							#查找失败,返回-1

R=[8,14,6,9,10,22,34,18,19,31,40,38,54,66,46,71,78,68,80,85,100,94,88,96,87]
b=5
I=[None]*b
CreateI(R,I,b)
print("索引块:")
for i in range(b):
    print("%d: [%d,%d]" %(i,I[i].key,I[i].link))
print("查找")
for i in range(len(R)):
    k=R[i]
    print("k=%d的位置:%d" %(k,BlkSearch(R,I,b,k)))
