import copy                                 #导入copy模块
class Set:								    #集合类
    MaxSize=100                             #集合的最多元素个数
    def __init__(self):				        #构造方法
        self.data=[None]*Set.MaxSize	    #data存放集合元素
        self.size=0                         #size为集合的长度

    def getsize(self):					    #返回集合的长度
        return self.size;

    def get(self,i):					    #返回集合的第i个元素
        assert i>=0 and i<self.size         #检测参数i的正确性
        return self.data[i]

    def IsIn(self,e):				        #判断e是否在集合中
        for i in range(self.size):
            if self.data[i]==e:
                return True
        return False

    def add(self,e):				        #将元素e添加到集合中
        if not self.IsIn(e):			    #元素e不在集合中
            self.data[self.size]=e
            self.size+=1

    def delete(self,e):			            #从集合中删除元素e
        i=0
        while i<self.size and self.data[i]!=e:
            i+=1
        if i>=self.size:
            return			                #未找到元素e直接返回
        for j in range(i+1,self.size):
            self.data[j-1]=self.data[j]
        self.size-=1

    def Copy(self):                         #返回当前集合的复制集合
        s1=Set()
        s1.data=self.data
        s1.size=self.size
        return s1
        
    def display(self):				        #输出集合中的元素
        for i in range(self.size):
            print(self.data[i],end=' ')
        print()

    def Union(self,s2):                     #求s3=s1∪s2(s1为当前集合)
        s3=self.Copy()                      #将当前集合复制到s3
        for i in range(s2.getsize()):	    #将s2中不在当前集合中的元素添加到s3中
            e=s2.get(i)
            if  not self.IsIn(e):
                s3.add(e)
        return s3					        #返回s3


    def Inter(self,s2):          	        #求s3=s1∩s2(s1为当前集合)
        s3=Set()
        for i in range(self.size):			#将s1中出现在s2中的元素复制到s3中
            e=self.data[i]
            if s2.IsIn(e):
                s3.add(e)
        return s3					        #返回s3
	
    def Diff(self,s2):                      #求s3=s1-s2(s1为当前集合)
        s3=Set()
        for i in range(self.size):          #将s1中不出现在s2中的元素复制到s3中
            e=self.data[i]
            if not s2.IsIn(e):
                s3.add(e)
        return s3					        #返回s3
	
#主程序
s1=Set()
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(6)
s1.add(8)
print("集合s1:",end=' '),s1.display()
print("s1的长度为%d" %(s1.getsize()))
s2=Set()
s2.add(2)
s2.add(5)
s2.add(3)
s2.add(6)
print("集合s2:",end=' '),s2.display()
print("集合s1和s2的并集->s3")
s3=s1.Union(s2);
print("集合s3:",end=' '),s3.display()
print("集合s1和s2的差集->s4")
s4=s1.Diff(s2)
print("集合s4:",end=' '),s4.display()
print("集合s1和s2的交集->s5")
s5=s1.Inter(s2)
print("集合s5:",end=' '),s5.display()

