from BTree import BTree,BTNode
def Level(bt,x):               	            #解法1
    return _Level(bt.b,x,1)
def _Level(t,x,h):
    if t==None:
        return 0								#空树不能找到该结点
    elif t.data==x:
        return h								#根结点即为所找,返回其层次
    else:
        l=_Level(t.lchild,x,h+1)			    #在左子树中查找
        if l!=0:
            return l						#左子树中找到了,返回其层次
        else:
            return _Level(t.rchild,x,h+1)	    #左子树中未找到,再在右子树中查找

'''
def Level2(bt,x):                           	#解法2
    return _Level2(bt.b,x)
def _Level2(t,x):
    if t==None:									#空树不能找到该结点
        return 0
    if t.data==x:								#根结点值为x
        return 1
    leftl=0 if t.lchild==None else _Level2(t.lchild,x)
    rightl=0 if t.rchild==None else _Level2(t.rchild,x)
    if leftl<1 and rightl<1:						#左右子树都没有找到，返回0
        return 0;
    return max(leftl,rightl)+1				#返回左右子树中最大层次+1
'''

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
x='C'
print(x+"的层次=%d" %(Level(bt,x)))
x='F'
print(x+"的层次=%d" %(Level(bt,x)))
x='X'
print(x+"的层次=%d" %(Level(bt,x)))

