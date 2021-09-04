#扩展拆半查找
def GOEk(R,k):					            #查找第一个大于或者等于k的序号即k的插入点
    n=len(R)
    low,high=0,n-1
    while low<=high:					    #当前区间非空时
        mid=(low+high)#2				    #求查找区间的中间位置
        if k<=R[mid]:				        #继续在R[low..mid-1]中查找
            high=mid-1
        else:							    #k>R[mid]
            low=mid+1					    #继续在R[mid+1..high]中查找
    return high+1						    #返回high+1

def Closest(R,k):
    n=len(R)
    if k<=R[0]: return R[0]
    if k>=R[n-1]: return R[s.n-1]
    j=GOEk(R,k)						#查找第一个大于或者等于k的序号
    i=j-1							#前一个元素的序号
    if abs(R[i]-k)<abs(R[j]-k):
        return R[i]
    else:
        return R[j]


R=[1,3,8,8,12]
k=6
res=Closest(R,k)
print(res)
k=10
res=Closest(R,k)
print(res)
