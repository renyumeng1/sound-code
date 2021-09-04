MAXN=100                            #堆中最多元素个数
class Heap:                         #堆数据结构的实现(默认大根堆)
    def __init__(self,d=None):      #构造方法
        self.R=[None]*MAXN          #存放堆中元素
        self.n=0                    #记录堆中元素个数

    def cmp(self,x,y):              #比较方法(大根堆)
        return x<y
        
    def siftDown(self,low,high):	#R[low..high]的自顶向下筛选
        i=low
        j=2*i+1				        #R[j]是R[i]的左孩子
        tmp=self.R[i]					#tmp临时保存根结点
        while j<=high:				#只对R[low..high]的元素进行筛选
            if j<high and self.cmp(self.R[j],self.R[j+1]):
                j+=1				#若右孩子较大,把j指向右孩子
            if self.cmp(tmp,self.R[j]):	#tmp的孩子较大
                self.R[i]=self.R[j]			#将R[j]调整到双亲位置上
                i,j=j,2*i+1			#修改i和j值,以便继续向下筛选
            else: break				#若孩子较小，则筛选结束
        self.R[i]=tmp					#原根结点放入最终位置

    def siftUp(self,j):		        #自底向上筛选:从叶子结点i向上筛选
        i=(j-1)//2   				#i指向R[j]的双亲
        while True:
            if self.cmp(self.R[i],self.R[j]): #若孩子较大
                self.R[i],self.R[j]=self.R[j],self.R[i]	#交换
            if i==0: break			#到达根结点时结束
            j=i
            i=(j-1)//2;				#继续向上调整

    def append(self,e):			    #插入元素e
        if self.n==MAXN: return     #堆满直接返回
        self.R[self.n]=e		    #将e添加到末尾
        self.n+=1				    #堆中元素个数增1
        if self.n==1:return;	    #e作为根结点的情况
        j=self.n-1
        self.siftUp(j)              #从叶子结点R[j]向上筛选

    def pop(self):				    #删除堆顶元素
        if self.n==1:
            self.n=0
            return self.R[0]
        e=self.R[0]				    #取出堆顶元素
        self.R[0]=self.R[self.n-1]  #用尾元素覆盖R[0]
        self.n-=1				    #元素个数减少1
        self.siftDown(0,self.n-1)   #筛选为一个堆
        return e

    def gettop(self):               #取堆顶元素
        return self.R[0]

    def empty(self):		        #判断堆是否为空
        return self.n==0

    def disp(self):
        for i in range(self.n):
            print(self.R[i],end=' ')
        print()

#主程序
if __name__ == '__main__':
    heapq=Heap()
    a=[1,2,3,4,5,6]
    for i in range(len(a)):
        heapq.append(a[i])
    print("初始序列",end=' ')
    print(a)
    print("排序")
    print("排序序列",end=' ')
    while not heapq.empty():
        print(heapq.pop(),end=' ')
