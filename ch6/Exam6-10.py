from BTree import BTree,BTNode
def Displeaf1(bt):	 	                        #基于先序遍历输出叶子结点
    _Displeaf1(bt.b)
def _Displeaf1(t):
    if t!=None:
        if t.lchild==None and t.rchild==None:
            print(t.data,end=' ')			    #输出叶子结点
        _Displeaf1(t.lchild)					#遍历左子树
        _Displeaf1(t.rchild)					#遍历右子树

def Displeaf2(bt):  	                        #基于中序遍历输出叶子结点
    _Displeaf2(bt.b)
def _Displeaf2(t):
    if t!=None:
        _Displeaf2(t.lchild)					#遍历左子树
        if t.lchild==None and t.rchild==None:
            print(t.data,end=' ')			    #输出叶子结点
        _Displeaf2(t.rchild)					#遍历右子树
def Displeaf3(bt):		                        #基于后序遍历输出叶子结点
    _Displeaf3(bt.b)
def _Displeaf3(t):
    if t!=None:
        _Displeaf2(t.lchild)					#遍历左子树
        _Displeaf2(t.rchild)					#遍历右子树
        if t.lchild==None and t.rchild==None:
            print(t.data,end=' ')			    #输出叶子结点
def Displeaf4(bt):		                        #基于递归算法思路
    _Displeaf4(bt.b)
def _Displeaf4(t):
    if t!=None:
        if t.lchild==None and t.rchild==None:
            print(t.data,end=' ')			    #输出叶子结点
        else:
            _Displeaf4(t.lchild)		        #遍历左子树
            _Displeaf4(t.rchild)				#遍历右子树

#主程序
b=BTNode('A')
p1=BTNode('B')
p2=BTNode('C')
p3=BTNode('D')
p4=BTNode('E')
p5=BTNode('F')
p6=BTNode('G')
b.lchild=p1
b.rchild=p2
p1.lchild=p3
p3.rchild=p6
p2.lchild=p4
p2.rchild=p5
bt=BTree()
bt.SetRoot(b)
print("bt:",end=' '); print(bt.DispBTree())
print("算法1 所有叶子结点",end=' ');Displeaf1(bt);print()
print("算法2 所有叶子结点",end=' ');Displeaf2(bt);print()
print("算法3 所有叶子结点",end=' ');Displeaf3(bt);print()
print("算法4 所有叶子结点",end=' ');Displeaf4(bt);print()
