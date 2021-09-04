alpha=0.75                              #全局变量,表示装填因子
class HNode:                            #单链表结点类
    def __init__(self,k,v):             #构造方法
        self.key=k                      #关键字
        self.v=v                        #值
        self.next=None

class Dict:                             #哈希表(除留余数法+拉链法)
    def __init__(self):                 #构造方法
        self.cap=8                      #设置初始容量为8,即哈希表长度m=8
        self.n=0                        #哈希表中元素个数
        self.ha=[None]*self.cap         #分配哈希表的cap个桶

    def resize(self):                   #按两倍扩大容量
        newha=[None]*2*self.cap
        self.n=0
        for i in range(self.cap):
            p=self.ha[i]
            while p!=None:
                d=hash(p.key) % self.cap    #求哈希函数值
                q=HNode(p.key,p.v)          #新建结点q
                q.next=newha[d]             #采用头插法将q插入到newha[d]单链表中
                newha[d]=q
                self.n+=1                   #哈希表元素个数增1
                p=p.next
        self.ha=newha
        self.cap=2*self.cap

    def insert(self,k,v):               #在哈希表中插入(k,v)
        if self.n>=int(alpha*self.cap): #若元素个数大于等于期望的元素个数
            self.resize()               #扩大容量
        p=self.search(k)                #查找关键字k
        if p!=None:                     #若存在关键字k
            p.v=v                       #更新v
        else:                           #若不存在关键字k，插入
            d=hash(k) % self.cap        #求哈希函数值
            p=HNode(k,v)                #新建关键字k的结点p
            p.next=self.ha[d]           #采用头插法将p插入到ha[d]单链表中
            self.ha[d]=p
            self.n+=1                   #哈希表元素个数增1

    def search(self,k):	                #查找关键字k,成功时返回其地址,否则返回空
        d=hash(k) % self.cap		    #求哈希函数值
        p=self.ha[d]                    #p指向ha[d]单链表的首结点
        while p!=None and p.key!=k:     #查找key为k的结点p
            p=p.next
        return p                        #返回p

    def __contains__(self,k):           #in运算符重载
        if self.search(k)!=None:
            return True
        else:
            return False

    def __getitem__(self,k):            #按关键字取值
        p=self.search(k)
        if p!=None:
            return p.v
        else:
            return None
    
    def __setitem__(self,k,d):          #按关键字赋值
        self.insert(k,d)

    def delete(self,k):                 #删除关键字k
        d=hash(k) % self.cap
        if self.ha[d]==None: return
        if self.ha[d].next==None:        #ha[d]只有一个结点
            if self.ha[d].key==k:
                self.ha[d]=None
            return
        pre=self.ha[d]                  #ha[d]有一个以上结点
        p=p.next
        while p!=None and p.key!=k:
            pre=p                       #pre和p同步后移
            p=p.next
        if p!=None:                     #找到关键字为k的结点p
            pre.next=p.next             #删除结点p

    def dispht(self):                   #输出所有元素
        for i in range(self.cap):
            p=self.ha[i]
            while p!=None:
                print("%3d[%d]" %(p.key,p.v),end='')
                p=p.next
            print()
 
#主程序
if __name__ == '__main__':
    a=[1,2,5,4,1,2,5,1,6,20,5,10,9,6]
    print("(1)建立dic")
    dic=Dict()
    print("  初始容量:",dic.cap)
    print("(2)插入若干元素")
    for i in range(len(a)):
        if a[i] in dic:             #若a[i]已存在，次数增1
            dic[a[i]]+=1
        else:                       #若a[i]不存在，次数置为1
            dic[a[i]]=1
    print("  容量:",dic.cap)
    print("(3)输出所有的元素：")
    dic.dispht()
    k=2
    print("(4)删除关键字%d" %(k))
    dic.delete(2)
    print("(5)删除后所有元素：")
    dic.dispht()
     
