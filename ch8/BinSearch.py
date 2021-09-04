def BinSearch1(R,k):				        #拆半查找非递归算法
    n=len(R)
    low,high=0,n-1
    while low<=high:						#当前区间非空时
        mid=(low+high)//2					#求查找区间的中间位置
        if k==R[mid]:					    #查找成功返回其序号mid
            return mid
        if k<R[mid]:					    #继续在R[low..mid-1]中查找
            high=mid-1
        else:								#k>R[mid]
            low=mid+1						#继续在R[mid+1..high]中查找
    return -1								#当前查找区间空时返回-1

def BinSearch2(R,k):				 		#拆半查找递归算法
    return BinSearch21(R,0,len(R)-1,k)

def BinSearch21(R,low,high,k):   		    #被BinSearch2方法调用
    if low<=high:						 	#当前查找区间非空时
        mid=(low+high)//2					#求查找区间的中间位置
        if k==R[mid]:						#查找成功返回其序号mid
            return mid
        if k<R[mid]:						#递归在左区间中查找
            return BinSearch21(R,low,mid-1,k)
        else:								#k>R[mid],递归在右区间中查找
            return BinSearch21(R,mid+1,high,k)
    else: return -1							#当前查找区间空时返回-1

#扩展拆半查找
def GOEk(R,k):					            #查找第一个大于或者等于k的序号即k的插入点
    n=len(R)
    low,high=0,n-1
    while low<=high:					    #当前区间非空时
        mid=(low+high)//2				    #求查找区间的中间位置
        if k<=R[mid]:				        #继续在R[low..mid-1]中查找
            high=mid-1
        else:							    #k>R[mid]
            low=mid+1					    #继续在R[mid+1..high]中查找
    return high+1						    #返回high+1

def Firstequalsk(R,k):				        #查找第一个等于k的元素序号
    n=len(R)
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if k<=R[mid]: high=mid
        else: low=mid+1
    if k==R[low]: return low
    else: return -1

def Lastequalsk(R,k):				        #查找最后一个等于k的元素序号
    n=len(R)
    low,high=0,n-1
    while low<high:
        mid=(low+high+1)//2
        if k>=R[mid]: low=mid
        else: high=mid-1
    if k==R[low]: return low
    else: return -1

def Intervalk(R,k):				            #查找为k的元素区间res
    res=[None]*2
    res[0]=Firstequalsk(R,k)
    res[1]=Lastequalsk(R,k)
    return res

R=[1,2,3,3,3]
k=2
res=GOEk(R,k)
print(res)
