from CSqQueue import CSqQueue

def pushk(qu,k,e):                     #进队第k个元素e
    n=qu.size()
    if k<1 or k>n+1:
        return False					#参数k错误返回False
    if k<=n:
        for i in range(1,n+1):          #循环处理队中所有元素
            if i==k:
                qu.push(e)				#将e元素进队到第k个位置
            x=qu.pop()					#出队元素x
            qu.push(x)					#进队元素x
    else:
        qu.push(e)						#k=n+1时直接进队e
    return True

def popk(qu,k):	                        #出队第k个元素
    n=qu.size()
    assert k>=1 and k<=n                 #检测参数k错误
    for i in range(1,n+1):				#循环处理队中所有元素
        x=qu.pop()						#出队元素x
        if i!=k:
            qu.push(x)					#将非第k个元素进队
        else:
            e=x							#取第k个出队的元素
    return e

#主程序
qu=CSqQueue()
qu.push(1)
qu.push(2)
qu.push(3)
qu.push(4)
print("元素个数=%d" %(qu.size()))
pushk(qu,1,5)
popk(qu,2)
while not qu.empty():
    print(qu.pop(),end=' ')
print()