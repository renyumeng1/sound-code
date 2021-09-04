from Heap import Heap
def Sort1(a):				#将递减排序
    heapq=Heap()
    n=len(a)
    for i in range(n):
        heapq.append(a[i])
    for j in range(n):
        a[j]=heapq.pop()

def Sort2(a):				#将递增排序
    heapq=Heap()
    n=len(a)
    for i in range(n):
        heapq.append(-a[i])
    for j in range(n):
        a[j]=-heapq.pop()

class MinHeap(Heap):            #创建小根堆类
    def cmp(self,x,y):          #比较方法(小根堆)
        return x>y
def Sort3(a):				    #递减排序
    heapq=MinHeap()
    n=len(a)
    for i in range(n):
        heapq.append(-a[i])
    for j in range(n):
        a[j]=-heapq.pop()

        
#主程序
if __name__ == '__main__':
    R=[9,8,7,6,5,4,3,2,1]
    Sort3(R)
    print(R)

