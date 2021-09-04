def BinInsertSort(R):					    #对R[0..n-1]按递增有序进行折半插入排序
    for i in range(1,len(R)):
        if R[i]<R[i-1]:				        #反序时
            tmp=R[i]						#将R[i]保存到tmp中
            low,high=0,i-1
            while low<=high:				#在R[low..high]中折半查找插入位置high+1
                mid=(low+high)//2			#取中间位置
                if tmp<R[mid]:
                    high=mid-1				#插入点在左区间
                else:
                    low=mid+1				#插入点在右区间
            for j in range(i-1,high,-1):    #元素集中后移
                R[j+1]=R[j]
            R[high+1]=tmp					#插入原来的R[i]

#主程序
if __name__ == '__main__':
    R=[9,8,7,6,5,4,3,2,1]
    #R=[1,3,4,2]
    print("初始序列",end=' ')
    print(R)
    print("排序")
    BinInsertSort(R)
    print("排序序列",end=' ')
    print(R)
