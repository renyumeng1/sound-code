import copy
from BTree import BTree,BTNode
def Ancestor1(bt,x):            	        #返回x结点的祖先
    res=[]
    _Ancestor1(bt.b,x,res)
    return res
def _Ancestor1(t,x,res):	
    if t==None:                             #空树返回空串
        return False
    if t.lchild!=None and t.lchild.data==x:
        res.append(t.data)		            #t结点是x结点的祖先
        return True
    if t.rchild!=None and t.rchild.data==x:
        res.append(t.data)		            #t结点是x结点的祖先
        return True
    if _Ancestor1(t.lchild,x,res) or  _Ancestor1(t.rchild,x,res):
        res.append(t.data)			        #t结点是x结点的祖先
        return True
    return False					        #其他情况返回False

res=[]                                      #全局变量,存放祖先
def Ancestor2(bt,x):			            #返回x结点的祖先
    global res
    path=[]
    res=[]
    _Ancestor2(bt.b,x,path)
    return res                              #返回祖先列表res

def _Ancestor2(t,x,path):
    global res
    if t==None: return                      #空树返回
    #print(t.data)                           #调试用：输出访问的结点
    path.append(t.data)
    if t.data==x:
        path.pop()					        #删除x结点
        res=copy.deepcopy(path)             #深复制
        return                              #找到后返回
    _Ancestor2(t.lchild,x,path)             #在左子树中查找
    _Ancestor2(t.rchild,x,path)	            #在右子树中查找
    path.pop()                              #x结点处理完毕，回退

def Ancestor3(bt,x):			            #返回x结点的祖先
    path=[]
    _Ancestor3(bt.b,x,path)
    return path                             #返回祖先列表res

def _Ancestor3(t,x,path):
    if t==None: return False                #空树返回
    #print(t.data)                           #调试用：输出访问的结点
    path.append(t.data)
    if t.data==x:
        path.pop()					        #删除x结点
        return True                         #找到后返回
    if _Ancestor3(t.lchild,x,path) or _Ancestor3(t.rchild,x,path):
        return True                         #在左或者右子树中查找
    else:
        path.pop()                          #x结点处理完毕，回退

#res=[]                                      #全局变量,存放祖先
def Ancestor4(bt,x):			            #返回x结点的祖先
    global res
    res=[]
    path=[None]*100
    d=-1
    _Ancestor4(bt.b,x,path,d)
    return res                              #返回祖先列表res

def _Ancestor4(t,x,path,d):
    global res
    if t==None: return False                #空树返回
    #print(t.data)                           #调试用：输出访问的结点
    d+=1;path[d]=t.data
    if t.data==x:
        for i in range(d):
            res.append(path[i])
        return True                         #找到后返回
    if _Ancestor4(t.lchild,x,path,d) or _Ancestor4(t.rchild,x,path,d):
        return True                         #在左或者右子树中查找


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
print("解法1 "+x+"的祖先: ",Ancestor1(bt,x))
print("解法2 "+x+"的祖先: ",Ancestor2(bt,x))
print("解法3 "+x+"的祖先: ",Ancestor3(bt,x))
print("解法4 "+x+"的祖先: ",Ancestor4(bt,x))
