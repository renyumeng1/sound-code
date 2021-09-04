from BTree import BTree,BTNode
def PreOrderSeq(bt):                #二叉树bt的序列化
    return _PreOrderSeq(bt.b)
def _PreOrderSeq(t):
    if t==None:	return ["#"]
    s=[t.data]				        #含根结点
    s+=_PreOrderSeq(t.lchild)		#产生左子树的序列化序列
    s+=_PreOrderSeq(t.rchild)		#产生右子树的序列化序列
    return s

'''
def CreateBTree3(s): 		        #由序列化序列s创建二叉链：反序列化
    global i
    i=0;
    bt=BTree()
    bt.SetRoot(_CreateBTree3(s))
    return bt
def _CreateBTree3(s):
    global i
    if i>=len(s): return None				#i超界返回空
    d=s[i];i+=1								#从s中取出一个元素d
    if d=="#": return None					#若d为"#"，返回空
    t=BTNode(d)         					#创建根结点(结点值为d
    t.lchild=_CreateBTree3(s)					#递归构造左子树
    t.rchild=_CreateBTree3(s)					#递归构造右子树
    return t								#返回根结点
'''

def CreateBTree3(s): 		        #由序列化序列s创建二叉链：反序列化
    bt=BTree()
    it=iter(s)                      #定义s的迭代器lt
    bt.SetRoot(_CreateBTree3(it))
    return bt
def _CreateBTree3(it):
    try:
        d=next(it)					#取下一个元素d
        if d=="#": return None		#若d为"#"，返回空
        t=BTNode(d)         		#创建根结点(结点值为d
        t.lchild=_CreateBTree3(it)	#递归构造左子树
        t.rchild=_CreateBTree3(it)	#递归构造右子树
        return t					#返回根结点
    except StopIteration:
        return None                 #若已经取完，返回空

b=BTNode('A')					    #建立各个结点
p1=BTNode('B')
p2=BTNode('C')
p3=BTNode('D')
p4=BTNode('E')
p5=BTNode('F')
p6=BTNode('G')
b.lchild=p1								#建立结点之间的关系
b.rchild=p2
p1.lchild=p3
p3.rchild=p6
p2.lchild=p4
p2.rchild=p5
bt=BTree()
bt.SetRoot(b)
print("bt:",end=' '); print(bt.DispBTree())
print("序列化->s")
s=PreOrderSeq(bt)
print(s)
print("s反序列化->bt2")
bt2=CreateBTree3(s)
print("bt2:",end=' '); print(bt2.DispBTree())
