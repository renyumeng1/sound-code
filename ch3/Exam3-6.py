class STACK:
    def __init__(self):                 #构造方法
        self.data=[]                    #存放主栈中元素，初始为空
        self.__mindata=[]               #存放min栈中元素，初始为空
    #min栈基本运算算法
    def __minempty(self):               #判断min栈是否空
        return len(self.__mindata)==0
    def __minpush(self,e):              #元素进min栈
        self.__mindata.append(e)        
    def __minpop(self):                 #元素出min栈
        assert not self.__minempty()    #检测min栈为空的异常
        return self.__mindata.pop()
    def __mingettop(self):              #取min栈栈顶元素
        assert not self.__minempty()    #检测min栈为空的异常
        return self.__mindata[-1];


    #主栈基本运算算法
    def empty(self):                    #判断主栈是否空
        return len(self.data)==0


    def push(self,x):                   #元素进主栈
        if self.empty() or  x<=self.Getmin():
            self.__mindata.append(x)    #栈空或者x<=min栈顶元素时进min栈
        self.data.append(x);            #将x进主栈

    def pop(self):                      #元素出主栈
        assert not self.empty()         #检测主栈为空的异常
        x=self.data.pop()               #从主栈出栈
        if x==self.__mingettop():	    #若栈顶元素为最小元素
            self.__minpop()             #min栈出栈一次
        return x

    def gettop(self):                   #取主栈栈顶元素
        assert not self.empty()         #检测主栈为空的异常
        return self.data[-1]


    def Getmin(self):			        #获取栈中最小元素
        assert not self.empty()		    #检测主栈为空的异常
        return self.__mindata[-1];      #返回min栈的栈顶元素即主栈中最小元素
#主程序
st=STACK()
print("\n  元素5,6,3,7依次进栈")
st.push(5)
st.push(6)
st.push(3)
st.push(7)
print("  求最小元素并出栈")
while not st.empty():
    print("    最小元素:%d" %(st.Getmin()))
    print("    出栈元素:%d" %(st.pop()))
print()
