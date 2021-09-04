from BTree import BTree,BTNode
from collections import deque

class QNode:								#队列元素类
    def __init__(self,l,p):     		    #构造方法
        self.lev=l							#结点的层次
        self.node=p					        #结点引用

def KCount1(bt,k):		                    #解法1：求二叉树第k层结点个数
    cnt=0								    #累计第k层结点个数
    qu=deque()                              #定义一个队列qu
    qu.append(QNode(1,bt.b))				#根结点(层次为1)进队
    while len(qu)>0:                    	#队不空循环
        p=qu.popleft()						#出队一个结点
        if p.lev>k:							#当前结点的层次大于k，返回
            return cnt
        if p.lev==k:
            cnt+=1							#当前结点是第k层的结点,cnt增1
        else:								#当前结点的层次小于k
            if p.node.lchild!=None:			#有左孩子时将其进队
                qu.append(QNode(p.lev+1,p.node.lchild))
            if p.node.rchild!=None:			#有右孩子时将其进队
                qu.append(QNode(p.lev+1,p.node.rchild))
    return cnt


def KCount2(bt,k):			                #解法2：求二叉树第k层结点个数
    cnt=0									#累计第k层结点个数
    qu=deque()                              #定义一个队列qu
    curl=1								    #当前层次,从1开始
    last=bt.b								#第1层最右结点
    qu.append(bt.b)							#根结点进队
    while len(qu)>0:                    	#队不空循环
        if curl>k:							#当层号大于k时返回cnt,不再继续
            return cnt
        p=qu.popleft()						#出队一个结点
        if curl==k:
            cnt+=1							#当前结点是第k层的结点,cnt增1
        if p.lchild!=None:					#有左孩子时将其进队
            q=p.lchild
            qu.append(q)
        if p.rchild!=None:					#有右孩子时将其进队
            q=p.rchild
            qu.append(q)
        if p==last:							#当前层的所有结点处理完毕
            last=q							#让last指向下一层的最右结点
            curl+=1
    return cnt

def KCount3(bt,k):			                #解法3：求二叉树第k层结点个数
    if k<1: return 0						#k<1返回0
    qu=deque()                              #定义一个队列qu
    curl=1								    #当前层次,从1开始
    qu.append(bt.b)							#根结点进队
    while len(qu)>0:                    	#队不空循环
        if curl==k:							#当前层为第k层，返回队中元素个数
            return len(qu)
        n=len(qu)							#求出当前层结点个数
        for i in range(n):					#出队当前层的n个结点
            p=qu.popleft()					#出队一个结点
            if p.lchild!=None:				#有左孩子时将其进队
                qu.append(p.lchild)
            if p.rchild!=None:				#有右孩子时将其进队
                qu.append(p.rchild)
        curl+=1								#转向下一层
    return 0

#主程序
b=BTNode('A')
p1=BTNode('B');p2=BTNode('C')
p3=BTNode('D');p4=BTNode('E')
p5=BTNode('F');p6=BTNode('G')
b.lchild=p1;b.rchild=p2
p1.lchild=p3;p3.rchild=p6
p2.lchild=p4;p2.rchild=p5
bt=BTree()
bt.SetRoot(b)
print("bt:",end='  ');print(bt.DispBTree())
print("解法1")
for i in range(6):
    print("   第%d层的结点个数=%d" %(i,KCount1(bt,i)))
print("解法2")
for i in range(6):
    print("   第%d层的结点个数=%d" %(i,KCount2(bt,i)))
print("解法3")
for i in range(6):
    print("   第%d层的结点个数=%d" %(i,KCount3(bt,i)))