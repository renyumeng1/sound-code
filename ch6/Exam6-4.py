class EBNode:					        #长子兄弟链中结点类
    def __init__(self,d=None):          #构造方法
        self.data=d				        #结点的值
        self.brother=None				#指向兄弟
        self.eson=None					#指向长子结点


def Height(t):
    if t==None:                         #空树返回0
        return 0
    maxsh=0
    p=t.eson;                           #p指向t结点的长子
    while p!=None:
        q=p.brother                     #q临时保存结点p的后继结点
        sh=Height(p)                    #递归求结点p的子树的高度
        maxsh=max(maxsh,sh)             #求结点t的所有子树的最大高度
        p=q
    return maxsh+1                      #返回maxsh+1   

#主程序
a=EBNode('A')
b=EBNode('B')
c=EBNode('C')
d=EBNode('D')
e=EBNode('E')
f=EBNode('F')
g=EBNode('G')
a.eson=b
b.eson=d
b.brother=c
d.brother=e
e.brother=f
e.eson=g
print(Height(a))
