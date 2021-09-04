class Stud2:                                #学生单链表结点类型
    def __init__(self,no1,name1,score1):    #构造函数
        self.no=no1
        self.name=name1
        self.score=score1
        self.next=None
    def __repr__(self):                     #输出学生结点的格式
        return str(self.no)+"\t\t"+self.name+"\t\t"+str(self.score)
    

class Store2:
    def __init__(self):                     #构造函数
        self.head=None
        
    def Create(self):                       #创建学生单链表
        self.head=Stud2(2018001,"王华",90)  #学生单链表首结点
        p2=Stud2(2018010,"刘丽",62)
        p3=Stud2(2018006,"陈明",54)
        p4=Stud2(2018009,"张强",95)
        p5=Stud2(2018007,"许兵",76)
        p6=Stud2(2018012,"李萍",88)
        p7=Stud2(2018005,"李英",82)
        self.head.next=p2                   #建立结点之间的关系
        p2.next=p3
        p3.next=p4
        p4.next=p5
        p5.next=p6
        p6.next=p7
        p7.next=None

    def display(self):                      #输出学生单链表
        p=self.head
        while p!=None:
            print(p)
            p=p.next

    def Findi(self,i):                      #查找序号为i的学生分数
        j=0
        p=self.head				            #p指向首结点
        while j<i and p!=None:
            j+=1
            p=p.next
        assert i>=0 and p!=None
        return p.score                      #i正确时返回分数


st=Store2()
st.Create()
print("学号\t\t姓名\t\t分数")
st.display()
i=2
print("序号为%d的学生分数=%d" %(i,st.Findi(i)))

 
