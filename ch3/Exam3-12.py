MaxSize=100                                 #全局变量，假设容量为100
class CSqQueue1:      			            #本例循环队列类
    def __init__(self):                     #构造方法
        self.data=[None]*MaxSize            #存放队列中元素
        self.front=0                        #队头指针
        self.count=0					    #队中元素个数	
	#队列的基本运算算法
    def empty(self):					    #判断队列是否为空
        return self.count==0
    def push(self,e):					    #元素e进队
        rear1=(self.front+self.count)%MaxSize;
        assert self.count!=MaxSize          #检测队满
        rear1=(rear1+1) % MaxSize
        self.data[rear1]=e
        self.count+=1			            #元素个数增1
    def pop(self):					        #出队元素
        assert not self.empty()			    #检测队空
        self.count-=1					    #元素个数减1
        self.front=(self.front+1)%MaxSize   #队头指针循环进1
        return self.data[self.front]
    def gethead(self):					    #取队头元素
        assert not self.empty()             #检测队空
        head=(self.front+1)%MaxSize         #求队头元素的位置
        return self.data[head]

if __name__ == '__main__':
    qu=CSqQueue1()
    qu.push(1)
    qu.push(2)
    qu.push(3)
    qu.push(4)
    print("队头元素: %d" %(qu.gethead()))
    print("出队顺序:",end=' ')
    while not qu.empty():
        print(qu.pop(),end=' ')
    print()
    
