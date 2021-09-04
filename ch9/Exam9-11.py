def Merge1(R,low,mid,high):         	    #R[low..mid]和R[mid+1..high]归并为R[low..high]
    global ans
    R1=[None]*(high-low+1)         	    #分配临时归并空间R1
    i,j,k=low,mid+1,0   				#k是R1的下标,i、j分别为第1、2段的下标
    while i<=mid and j<=high:			#在第1段和第2段均未扫描完时循环
        if R[i]>R[j]:			      	#将第2段中的元素放入R1中
            R1[k]=R[j]
            ans+=mid-i+1                #累计逆序数
            j,k=j+1,k+1
        else:				          	#将第1段中的元素放入R1中
            R1[k]=R[i]
            i,k=i+1,k+1 
    while i<=mid:						#将第1段余下部分复制到R1
        R1[k]=R[i]
        i,k=i+1,k+1
    while j<=high:						#将第2段余下部分复制到R1
        R1[k]=R[j]
        j,k=j+1,k+1
    R[low:high+1]=R1[0:high-low+1]		#将R1复制回R中

def MergeSort1(R):				  	    #对R[0..n-1]按递增进行二路归并算法
	MergeSort11(R,0,len(R)-1);

def MergeSort11(R,s,t):         	    #被MergeSort2调用
    if s>=t: return						#R[s..t]的长度为0或者1时返回
    m=(s+t)//2						    #取中间位置m
    MergeSort11(R,s,m)					#对前子表排序
    MergeSort11(R,m+1,t)				#对后子表排序
    Merge1(R,s,m,t)						#将两个有序子表合并成一个有序表


#解法2
def MergeSort2(R):				  	    #对R[0..n-1]按递增进行二路归并算法
	MergeSort21(R,0,len(R)-1);

def MergeSort21(R,s,t):         	    #被MergeSort2调用
    if s>=t: return						#R[s..t]的长度为0或者1时返回
    m=(s+t)//2						    #取中间位置m
    MergeSort21(R,s,m)					#对前子表排序
    MergeSort21(R,m+1,t)				#对后子表排序
    Merge2(R,s,m,t)						#将两个有序子表合并成一个有序表


def Merge2(R,low,mid,high):             #R[low..mid]和R[mid+1..high]归并为R[low..high]
    global ans
    R1=[None]*(high-low+1)         	    #分配临时归并空间R1
    i,j,k=low,mid+1,0   				#k是R1的下标,i、j分别为第1、2段的下标
    while i<=mid and j<=high:			#在第1段和第2段均未扫描完时循环
        if R[i]<=R[j]:			      	#将第2段中的元素放入R1中
            R1[k]=R[i]
            ans+=j-mid-1                #累计逆序数
            i,k=i+1,k+1
        else:				          	#将第1段中的元素放入R1中
            R1[k]=R[j]
            j,k=j+1,k+1 
    while i<=mid:						#将第1段余下部分复制到R1
        R1[k]=R[i]
        ans+=high-mid
        i,k=i+1,k+1
    while j<=high:						#将第2段余下部分复制到R1
        R1[k]=R[j]
        j,k=j+1,k+1
    R[low:high+1]=R1[0:high-low+1]		#将R1复制回R中

a=[2,8,0,3]
ans=0
MergeSort1(a)
print("ans:",ans)
a=[2,8,0,3]
ans=0
MergeSort2(a)
print("ans:",ans)
