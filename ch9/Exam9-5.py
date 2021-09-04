def Partition1(R,s,t):				#划分算法1
    base=R[s]						#以表首元素为基准
    i,j=s,t
    while i<j:						#从表两端交替向中间遍历,直至i=j为止
        while i<j and R[j]>=base:
            j-=1					#从后向前遍历,找一个小于基准的R[j]
        while i<j and R[i]<=base:
            i+=1					#从前向后遍历,找一个大于基准的R[i]
        if i<j:
            R[i],R[j]=R[j],R[i]     #将R[i]和R[j]进行交换
    R[s],R[i]=R[i],R[s]             #将基准R[s]和R[i]进行交换
    return i

def Partition2(R,s,t):			    #划分算法2
    i,j=s,t
    base=R[s]						#以表首元素为基准
    while i!=j:						#从表两端交替向中间遍历,直至i=j为止
        while j>i and R[j]>=base:
            j-=1					#从后向前遍历,找一个小于基准的R[j]
        if j>i:
            R[i]=R[j]				#R[j]前移覆盖R[i]
            i+=1
        while i<j and R[i]<=base:
            i+=1					#从前向后遍历,找一个大于基准的R[i]
        if i<j:
            R[j]=R[i]				#R[i]后移覆盖R[j]
            j-=1
    R[i]=base						#基准归位
    return i						#返回归位的位置

def Partition3(R,s,t):   			#划分算法3
    i,j=s,s+1
    base=R[s]						#以表首元素为基准
    while j<=t:						#j从s+1开始遍历其他元素
        if R[j]<=base:				#找到小于等于基准的元素R[j]
            i+=1					#扩大小于等于base的元素区间
            if i!=j:
                R[i],R[j]=R[j],R[i] #将R[i]与R[j]交换
        j+=1						#继续扫描
    R[s],R[i]=R[i],R[s]             #将基准R[s]和R[i]进行交换
    return i


def QuickSort2(R,s,t):
    if s<t: 				 		#表中至少存在两个元素的情况
        mid=(s+t)//2
        R[s],R[mid]=R[mid],R[s]     #R[s]与R[mid]交换
        i=Partition1(R,s,t)			#可以使用前面3种划分算法中的任意一种
        QuickSort2(R,s,i-1)			#对左子表递归排序
        QuickSort2(R,i+1,t)			#对右子表递归排序


#主程序
if __name__ == '__main__':
    R=[9,8,7,6,5,4,3,2,1]
    #R=[1,3,4,2]
    print("初始序列",end=' ')
    print(R)
    print("排序")
    QuickSort2(R,0,len(R)-1)
    print("排序序列",end=' ')
    print(R)
