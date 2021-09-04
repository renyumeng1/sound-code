from BTree import BTree,BTNode
def CopyBTree1(bt1):				#基于先序遍历复制二叉树
    bt2=BTree()
    bt2.SetRoot(_CopyBTree1(bt1.b))
    return bt2

def _CopyBTree1(t1):	#由t1复制产生t2
    if t1==None:
        return None
    else:
        t2=BTNode(t1.data) 	#复制根结点
        t2.lchild=_CopyBTree1(t1.lchild)								#递归复制左子树
        t2.rchild=_CopyBTree1(t1.rchild)								#递归复制右树
        return t2

def CopyBTree2(bt1):			#基于后序遍历复制二叉树
    bt2=BTree()
    bt2.SetRoot(_CopyBTree2(bt1.b))
    return bt2
def _CopyBTree2(t1):	#由t1复制产生t2
    if t1==None:
        return None
    else:
        l=_CopyBTree2(t1.lchild)								#递归复制左子树
        r=_CopyBTree2(t1.rchild)								#递归复制左子树
        t2=BTNode(t1.data)	#复制根结点
        t2.lchild=l
        t2.rchild=r
        return t2

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
print("bt:",end='  ');print(bt.DispBTree())
print("bt->bt2")
bt2=CopyBTree1(bt)
print("bt2:",end=' ');print(bt2.DispBTree())
print("bt->bt3")
bt3=CopyBTree2(bt)
print("bt3:",end=' ');print(bt3.DispBTree())

