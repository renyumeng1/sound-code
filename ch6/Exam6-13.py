from BTree import BTree,BTNode
def Trans(sb):                          #由顺序存储结构sb创建二叉链
    bt=BTree();
    bt.SetRoot(_Trans(sb,0))			#以sb[1]为根创建二叉链
    return bt

def _Trans(sb,i): 	                    #被Trans函数调用
    if i<len(sb)-1:
        if sb[i]!='#':
            t=BTNode(sb[i])             #建立根结点
            t.lchild=_Trans(sb,2*i+1)	#递归转换左子树
            t.rchild=_Trans(sb,2*i+2)	#递归转换右子树
            return t
        else: return None;			    #'#'结点返回空
    else: return None;					#无效结点返回空

#主程序
sb="ABCDE#F##GH##I######"
bt=Trans(sb)
print("bt:",end='  ');print(bt.DispBTree())
