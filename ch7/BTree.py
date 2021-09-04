from collections import deque
class BTNode:							            #二叉链中结点类
	def __init__(self,d=None):     		            #构造方法
		self.data=d						            #结点值
		self.lchild=None				            #左孩子指针
		self.rchild=None				            #右孩子指针
    
class BTree:                                        #二叉树类
    def __init__(self,d=None):     		            #构造方法
        self.b=None                                 #根结点指针
    def SetRoot(self,r):                            #设置根结点为r
        self.b=r
    def DispBTree(self):					        #返回二叉链的括号表示串
        return self._DispBTree1(self.b)
    def _DispBTree1(self,t):		                #被DispBTree方法调用
        if t==None:                                 #空树返回空串
            return ""
        else:
            bstr=t.data							    #输出根结点值
            if t.lchild!=None or t.rchild!=None:
                bstr+="("							#有孩子结点时输出"("
                bstr+=self._DispBTree1(t.lchild)	#递归输出左子树
                if t.rchild!=None:
                    bstr+=","						#有右孩子结点时输出","
                bstr+=self._DispBTree1(t.rchild)	#递归输出右子树
                bstr+=")"							#输出")"
            return bstr

    def FindNode(self,x):	                        #查找值为x的结点算法
        return self._FindNode1(b,x)
    def _FindNode1(self,t,x):                       #被FindNode方法调用
        if t==None: 
            return None								#t为空时返回null
        elif t.data==x: 
            return t								#t所指结点值为x时返回t
        else:
            p=self._FindNode1(t.lchild,x)			#在左子树中查找
            if p!=None: 
                return p							#在左子树中找到p结点，返回p
            else:
                return self._FindNode1(t.rchild,x)	#返回在右子树中查找结果

    def Height(self):								#求二叉树高度的算法
        return self._Height1(b)
    def _Height1(self,t):                            #被Height方法调用
        if t==None:
            return 0								#空树的高度为0
        else:
            lh=self._Height1(t.lchild)				#求左子树高度lchildh
            rh=self._Height1(t.rchild)				#求右子树高度rchildh
            return max(lh,rh)+1

def PreOrder(bt):				                    #先序遍历的递归算法
    PreOrder1(bt.b)
def PreOrder1(t):                                   #被PreOrder方法调用
    if t!=None:
        print(t.data,end=' ')					    #访问根结点
        PreOrder1(t.lchild)						    #先序遍历左子树
        PreOrder1(t.rchild)						    #先序遍历右子树
def InOrder(bt):               				        #中序遍历的递归算法
    InOrder1(bt.b)
def InOrder1(t):                     	            #被InOrder方法调用
    if t!=None:
        InOrder1(t.lchild)					        #中序遍历左子树
        print(t.data,end=' ')					    #访问根结点
        InOrder1(t.rchild)						    #中序遍历右子树
def PostOrder(bt):       		                    #后序遍历的递归算法
    PostOrder1(bt.b)
def PostOrder1(t):                                  #被PostOrder方法调用
    if t!=None:
        PostOrder1(t.lchild)					    #后序遍历左子树
        PostOrder1(t.rchild)					    #后序遍历右子树
        print(t.data,end=' ')					    #访问根结点
	
def LevelOrder(bt):         			            #层次遍历的算法
    qu=deque()                                      #将双端队列作为普通队列qu
    qu.append(bt.b)						            #根结点进队
    while len(qu)>0:                                #队不空循环
        p=qu.popleft()					            #出队一个结点
        print(p.data,end=' ')			            #访问p结点
        if p.lchild!=None:				            #有左孩子时将其进队
            qu.append(p.lchild)
        if p.rchild!=None:				            #有右孩子时将其进队
            qu.append(p.rchild)

if __name__ == '__main__':
    b=BTNode('A')							        #建立各个结点
    p1=BTNode('B')
    p2=BTNode('C')
    p3=BTNode('D')
    p4=BTNode('E')
    p5=BTNode('F')
    p6=BTNode('G')
    b.lchild=p1								        #建立结点之间的关系
    b.rchild=p2
    p1.lchild=p3
    p3.rchild=p6
    p2.lchild=p4
    p2.rchild=p5
    bt=BTree()
    bt.SetRoot(b)
    print("bt:",end=' '); print(bt.DispBTree())
    x='X'
    p=bt.FindNode(x)
    if p!=None: print("bt中存在"+x)
    else: print("bt中不存在"+x)
    print("bt的高度=%d" %(bt.Height()))
    print("先序序列:",end=' ');PreOrder(bt);print()
    print("中序序列:",end=' ');InOrder(bt);print()
    print("后序序列:",end=' ');PostOrder(bt);print()
    print("层次序列:",end=' ');LevelOrder(bt);print()
