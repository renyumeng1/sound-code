class TupElem:						    #三元组元素类
    def __init__(self,r1,c1,d1):        #构造方法
        self.r=r1                       #行号
        self.c=c1						#列号
        self.d=d1						#元素值
class TupClass:							#三元组表示类
    def __init__(self,rs,cs,ns):        #构造方法
        self.rows=rs					#行数
        self.cols=cs					#列数
        self.nums=ns					#非零元素个数
        self.data=[]					#稀疏矩阵对应的三元组顺序表
