def BSearch1(R,k):
    n=len(R)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if k==R[mid]: return mid
        if k<R[mid]: high=mid-1
        else: low=mid
    return -1

def BSearch2(R,k):
    n=len(R)
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if k==R[mid]: return mid
        if k<R[mid]: high=mid-1
        else: low=mid+1
    if R[low]==k: return low
    else: return -1

R=[1,3,5]
k=2
res=BSearch2(R,k)
print(res)
