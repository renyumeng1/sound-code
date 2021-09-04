class SonNode:         	            #孩子链存储结构结点类
    def __init__(self,d=None):      #构造方法
        self.data=d                 #结点的值
        self.sons=[]				#指向孩子结点的指针列表

def Height(t):                      #求t的高度
    if len(t.sons)==0:              #叶子结点的高度为1
        return 1
    maxsh=0
    for i in range(len(t.sons)):    #遍历所有子树
        sh=Height(t.sons[i])        #求子树t.sons[i]的高度
        maxsh=max(maxsh,sh)         #求所有子树的最大高度
    return maxsh+1        
        
        
a=SonNode('A')
b=SonNode('B')
c=SonNode('C')
d=SonNode('D')
e=SonNode('E')
f=SonNode('F')
g=SonNode('G')
a.sons.append(b)
a.sons.append(c)
b.sons.append(d)
b.sons.append(e)
b.sons.append(f)
e.sons.append(g)
print(Height(a))
