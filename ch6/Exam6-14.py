from BTree import BTree,BTNode

def KCount(bt,k):	                #算法1：求二叉树第k层结点个数
    global cnt
    cnt=0;
    _KCount(bt.b,1,k);
    return cnt
def _KCount(t,h,k):
    global cnt
    if t==None: return				#空树返回
    if h==k: cnt+=1					#当前层的结点在第k层，cnt增1
    if h<k:							#当前层次小于k，递归处理左、右子树
        _KCount(t.lchild,h+1,k)
        _KCount(t.rchild,h+1,k)

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
for i in range(6):
    print("第%d层结点个数: %d" %(i,KCount(bt,i)))
