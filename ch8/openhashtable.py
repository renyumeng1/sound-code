NULLKEY=None                            #全局变量,空关键字
class HashTable1:                       #哈希表(除留余数法+线性探测法)
    def __init__(self,m,p):             #构造方法
        self.n=0                        #哈希表中元素个数
        self.m=m
        self.p=p
        self.ha=[NULLKEY]*m             #存放哈希表元素
        
    def insert(self,k,v):               #在哈希表中插入(k,v)  
        d=k % self.p                    #求哈希函数值
        while self.ha[d]!=NULLKEY:      #找空位置
            d=(d+1) % self.m			#线性探测法查找空位置				
        self.ha[d]=[k,v]                #放置k
        self.n+=1                       #增加一个元素

    def search(self,k):	                #查找关键字k,成功时返回其位置，否则返回-1
        d=k % self.p				    #求哈希函数值
        while self.ha[d]!=NULLKEY and self.ha[d][0]!=k:
            d=(d+1) % self.m			#线性探测法查找空位置				
        if self.ha[d][0]==k:			#查找成功返回其位置
            return d
        else:						    #查找失败返回-1
            return -1

    def delete(self,k):                 #删除关键字k
        i=self.search(k)
        if i!=-1:
            self.ha[i]=NULLKEY
            self.n-=1

    def dispht(self):                   #输出哈希表
        for i in range(self.m):
            print("%4d" %(i),end='')
        print()
        for i in range(self.m):
            if self.ha[i]==None:
                print("    ",end='')
            else:
                print("%4d" %(self.ha[i][0]),end='')
        print()
 
    def ASL(self):                      #求成功情况下平均查找长度
        sum=0
        for i in range(self.m):
            if self.ha[i]!=NULLKEY:
                sum1=0
                k=self.ha[i][0]
                d=k % self.p		    #求哈希函数值
                sum1+=1
                while self.ha[d]!=NULLKEY and self.ha[d][0]!=k:
                    d=(d+1) % self.m	#线性探测法查找下一个位置				
                    sum1+=1
                print("key=%d 次数=%d" %(k,sum1))
                sum+=sum1
        return sum/self.n
            
    
a=[16,74,60,43,54,90,46,31,29,88,77]
n=len(a)
m=13
p=13
hashtable=HashTable1(m,p)
for i in range(len(a)):
    hashtable.insert(a[i],None)
print("哈希表")
hashtable.dispht()
print("ASL=%g" %(hashtable.ASL()))
