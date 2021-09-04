def BubbleSort(R):  				    #对R[0..n-1]按递增有序进行冒泡排序
    for i in range(len(R)-1): 
        exchange=False					#本趟前将exchange置为false
        for j in range(len(R)-1,i,-1):	#一趟中找出最小关键字的元素
            if R[j]<R[j-1]:         	#反序时交换
                R[j],R[j-1]=R[j-1],R[j] #R[j]和R[j-1]交换,将最小元素前移
                exchange=True			#本趟发生交换置exchange为true
        if exchange==False: return	    #本趟没有发生交换，中途结束算法

#主程序
if __name__ == '__main__':
    #R=[9,8,7,6,5,4,3,2,1]
    R=[1,3,4,2]
    print("初始序列",end=' ')
    print(R)
    print("排序")
    BubbleSort(R)
    print("排序序列",end=' ')
    print(R)
