class HNode:                            #单链表结点类
    def __init__(self,k,v):             #构造方法
        self.key=k
        self.v=v
        self.next=None
    
class HashTable2:                       #哈希表(除留余数法+拉链法)
    def __init__(self,m):               #构造方法
        self.n=0                        #哈希表中元素个数
        self.m=m                        #头结点空间[0..m-1]
        self.ha=[None]*m                #分配哈希表的m个桶
        
    def insert(self,k,v):               #在哈希表中插入(k,v)  
        d=k % self.m                    #求哈希函数值
        p=HNode(k,v)                    #新建关键字k的结点p
        p.next=self.ha[d]               #采用头插法将p插入到ha[d]单链表中
        self.ha[d]=p
        self.n+=1                       #哈希表元素个数增1

    def search(self,k):	                #查找关键字k,成功时返回其地址，否则返回空
        d=k % self.m				    #求哈希函数值
        p=self.ha[d]                    #p指向ha[d]单链表的首结点
        while p!=None and p.key!=k:     #查找key为k的结点p
            p=p.next
        return p                        #返回p

    def delete(self,k):                 #删除关键字k
        d=k % self.m
        if self.ha[d]==None: return
        if self.ha[d].next==None:        #ha[d]只有一个结点
            if self.ha[d].key==k:
                self.ha[d]=None
            return
        pre=self.ha[d]                  #ha[d]有一个以上结点
        p=pre.next
        while p!=None and p.key!=k:
            pre=p                       #pre和p同步后移
            p=p.next
        if p!=None:                     #找到关键字为k的结点p
            pre.next=p.next             #删除结点p

    def dispht(self):                   #输出哈希表
        for i in range(self.m):
            print("%4d:" %(i),end='')
            p=self.ha[i]
            while p!=None:
                print("%3d" %(p.key),end='')
                p=p.next
            print()
 

a=[16,74,60,43,54,90,46,31,29,88,77]
n=len(a)
m=13
ht=HashTable2(m)
for i in range(len(a)):
    ht.insert(a[i],None)
print("哈希表")
ht.dispht()
print("删除60")
ht.delete(60)
print("哈希表")
ht.dispht()
