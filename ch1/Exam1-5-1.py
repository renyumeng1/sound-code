class Stud1:                                    #高等数学成绩表学生顺序表元素类型
    def __init__(self,no1,name1,score1):        #构造函数
        self.no=no1
        self.name=name1
        self.score=score1
    def __repr__(self):                         #输出学生元素的格式
        return str(self.no)+"\t\t"+self.name+"\t\t"+str(self.score)
    
class Store1:                                   #学生顺序表类
    def __init__(self):                         #构造函数
        self.data=[]
        
    def Create(self):                           #创建学生顺序表
        self.data.append(Stud1(2018001,"王华",90))
        self.data.append(Stud1(2018010,"刘丽",62))
        self.data.append(Stud1(2018006,"陈明",54))
        self.data.append(Stud1(2018009,"张强",95))
        self.data.append(Stud1(2018007,"许兵",76))
        self.data.append(Stud1(2018012,"李萍",88))
        self.data.append(Stud1(2018005,"李英",82))

    def display(self):                          #输出学生顺序表
        print("学号\t\t姓名\t\t分数")
        for i in range(len(self.data)):
            print(self.data[i])

    def Findi(self,i):                          #查找序号为i的学生分数
        assert i>=0 and i<len(self.data)
        return self.data[i].score;              #i正确时返回分数


st=Store1()
st.Create()
st.display()
i=2
print("序号为%d的学生分数=%d" %(i,st.Findi(i)))

 
