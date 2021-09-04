from BTree import BTree,BTNode
def CreateBTree1(pres,ins):                #由先序序列pres和中序序列ins构造二叉链
    bt=BTree()
    bt.b=_CreateBTree1(pres,0,ins,0,len(pres))
    return bt
def _CreateBTree1(pres,i,ins,j,n):          #被CreateBTree1调用
    if n<=0: return None
    d=pres[i]                                   #取根结点值d
    t=BTNode(d)							         #创建根结点(结点值为d)
    p=ins.index(d)                                  #在ins中找到根结点的索引
    k=p-j											#确定左子树中结点个数k
    t.lchild=_CreateBTree1(pres,i+1,ins,j,k)		    #递归构造左子树
    t.rchild=_CreateBTree1(pres,i+k+1,ins,p+1,n-k-1)	#递归构造右子树
    return t

def CreateBTree2(posts,ins):                  #由后序序列posts和中序序列ins构造二叉链
    bt=BTree()
    bt.b=_CreateBTree2(posts,0,ins,0,len(posts))
    return bt;
def _CreateBTree2(posts,i,ins,j,n):
    if n<=0: return None
    d=posts[i+n-1]							        #取后序序列尾元素d
    t=BTNode(d) 						            #创建根结点(结点值为d)
    p=ins.index(d)                                  #在ins中找到根结点的索引
    k=p-j											#确定左子树中结点个数k
    t.lchild=_CreateBTree2(posts,i,ins,j,k)			#递归构造左子树
    t.rchild=_CreateBTree2(posts,i+k,ins,p+1,n-k-1)	#递归构造右子树
    return t

pres=['A','B','D','G','C','E','F']
ins=['D','G','B','A','E','C','F']
posts=['G','D','B','E','F','C','A']
print("先序:",end=' '); print(pres)
print("中序:",end=' '); print(ins)
print("构造二叉树bt1")
bt1=BTree()
bt1=CreateBTree1(pres,ins)
print("bt1:",end=' '); print(bt1.DispBTree())

print("后序:",end=' '); print(posts)
print("中序:",end=' '); print(ins)
print("构造二叉树bt2")
bt2=BTree()
bt2=CreateBTree2(posts,ins)
print("bt2:",end=' '); print(bt2.DispBTree())
