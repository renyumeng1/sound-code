MaxSize=100                             #假设容量为100
class SqQueue:      			        #非循环队列类
    def __init__(self):                 #构造方法
        self.data=[None]*MaxSize        #存放队列中元素
        self.front=-1                   #队头指针
        self.rear=-1                    #队尾指针
    def empty(self):				    #判断队列是否为空
        return self.front==self.rear
    def push(self,e):				    #元素e进队
        assert not self.rear==MaxSize-1      #检测队满
        self.rear+=1
        self.data[self.rear]=e
    def pop(self):						#出队元素
        assert not self.empty()         #检测队空
        self.front+=1
        return self.data[self.front]
    def gethead(self):					#取队头元素
        assert not self.empty()         #检测队空
        return self.data[self.front+1]

if __name__ == '__main__':
    qu=SqQueue()
    qu.push(1)
    qu.push(2)
    qu.push(3)
    while not qu.empty():
        print(qu.pop(),end=' ')
    print()
    