from BTree import BTree,BTNode
from collections import deque

class QNode:								#队列元素类
    def __init__(self,p,pre):     		    #构造方法
        self.node=p					        #当前结点引用
        self.pre=pre                        #当前结点的双亲结点                          
def Ancestor4(bt,x):            		    #层次遍历求x结点的祖先
    res=[]                                  #存放x结点的祖先
    qu=deque()                              #定义一个队列qu
    qu.append(QNode(bt.b,None))			    #根结点(双亲为None)进队
    while len(qu)>0:                    	#队不空循环
        p=qu.popleft()						#出队一个结点
        if p.node.data==x:					#当前结点p为x结点
            q=p.pre							#q为双亲
            while q!=None:					#找到根结点为止
                res.append(q.node.data)
                q=q.pre
            return res
        if p.node.lchild!=None:					#有左孩子时将其进队
            qu.append(QNode(p.node.lchild,p))	#置其双亲为p
        if p.node.rchild!=None:					#有右孩子时将其进队
            qu.append(QNode(p.node.rchild,p))	#置其双亲为p
    return res

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
x='G'
print(x+"结点的祖先:",Ancestor4(bt,x))
