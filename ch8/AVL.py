
class AVLNode:                          #AVL树结点类
    def __init__(self,k,d):             #构造方法，新建结点均为叶子，高度为1
        self.key=k                      #关键字k
        self.data=d                     #关键字对应的值d
        self.lchild=None                #左指针
        self.rchild=None                #右指针
        self.ht=1                       #当前结点的子树高度

class AVLTree:                          #AVL树类
    def __init__(self):
        self.r=None                     #根结点

    def getht(self,p):                  #返回结点p的子树高度
        if p==None: return 0
        return p.ht

    def right_rotate(self,a):           #以结点a为根做右旋转
        b=a.lchild
        a.lchild=b.rchild
        b.rchild=a
        a.ht=max(self.getht(a.rchild),self.getht(a.lchild))+1
        b.ht=max(self.getht(b.rchild),self.getht(b.lchild))+1
        return b

    def left_rotate(self,a):            #以结点a为根做左旋转
        b=a.rchild
        a.rchild=b.lchild
        b.lchild=a
        a.ht=max(self.getht(a.rchild),self.getht(a.lchild))+1
        b.ht=max(self.getht(b.rchild),self.getht(b.lchild))+1
        return b

    def LL(self,a):                     #LL型调整
        return self.right_rotate(a)

    def RR(self,a):                     #RR型调整
        return self.left_rotate(a)

    def LR(self,a):                     #LR型调整
        b=a.lchild
        a.lchild=self.left_rotate(b)    #结点b左旋
        return self.right_rotate(a)     #结点a右旋

    def RL(self,a):                     #RL型调整
        b=a.rchild
        a.rchild=self.right_rotate(b)   #结点b右旋
        return self.left_rotate(a)      #结点a左旋

    def insert(self,k,d):                 #插入(k,d)
        self.r=self._insert(self.r,k,d)
        #return self.r
        
    def _insert(self,p,k,d):
        if p==None:                             #空树时创建根结点
            q=AVLNode(k,d)
            return q
        elif k==p.key:
            p.data=d                            #更新d
            return p
        elif k<p.key:                           #k<p.key的情况
            p.lchild=self._insert(p.lchild,k,d) #将(k,d)插入到p的左子树中
            if self.getht(p.lchild)-self.getht(p.rchild)>=2: #找到失衡结点p
                if k<p.lchild.key:             #(k,d)是插入在p的左孩子的左子树中
                    p=self.LL(p)                #采用LL型调整
                else:                           #(k,d)是插入在p的左孩子的右子树中
                    p=self.LR(p)                #采用LR型调整
        else:                                   #k>p.key的情况
            p.rchild=self._insert(p.rchild,k,d) #将(k,d)插入到p的右子树中
            if self.getht(p.rchild)-self.getht(p.lchild)>=2:    #找到失衡结点p
                if k>p.rchild.key:              #(k,d)是插入在p的右孩子的右子树中
                    p=self.RR(p)                #采用RR型调整
                else:                           #(k,d)是插入在p的右孩子的左子树中
                    p=self.RL(p)                #采用RL型调整
        p.ht=max(self.getht(p.lchild),self.getht(p.rchild))+1   #更新结点p的高度
        return p

    def delete(self,k):                         #删除k
        self.r=self._delete(self.r,k)

    # 删除data结点
    def _delete(self,p,k):
        if p==None: return p
        if p.key==k:                        #找到关键字为k的结点p
            if p.lchild==None:              #结点p只有右子树的情况
                return p.rchild             #直接用右孩子替代结点p
            elif p.rchild==None:            #结点p只有左子树的情况
                return p.lchild             #直接用左孩子替代结点p
            else:                           #结点p同时有左右子树的情况
                if self.getht(p.lchild)>self.getht(p.rchild): #结点p的左子树较高
                    q=p.lchild
                    while(q.rchild!=None):  #在结点p的左子树中查找最大结点q
                        q=q.rchild
                    p=self._delete(p,q.key) #删除结点q
                    p.key=q.key             #用q结点值替代p结点值
                    p.data=q.data
                    return p
                else:                       #结点p的右子树较高
                    q=p.rchild
                    while q.lchild!=None:   #在结点p的右子树中查找最小结点q
                        q=q.lchild
                    p=self._delete(p,q.key) #删除结点q
                    p.key=q.key             #用q结点值替代p结点值
                    p.data=q.data
                    return p
        elif k<p.key:                       #k<p.key的情况
            p.lchild=self._delete(p.lchild,k)#在左子树中删除关键字k的结点
            if self.getht(p.rchild)-self.getht(p.lchild)>=2: #找到失衡结点p
                if self.getht(p.rchild.lchild)>self.getht(p.rchild.rchild):
                    #print("以%d做RL调整" %(p.key))
                    p=self.RL(p)                #若结点p的右孩子的左子树较高,做RL型调整
                else:
                    #print("以%d做RR型调整" %(p.key))
                    p=self.RR(p)                #若结点p的右孩子的右子树较高,做RR型调整
        elif k>p.key:                           #k>p.key的情况
            p.rchild=self._delete(p.rchild,k)   #在右子树中删除关键字k的结点
            if self.getht(p.lchild)-self.getht(p.rchild)>=2: #找到失衡结点p
                if self.getht(p.lchild.rchild)>self.getht(p.lchild.lchild):
                    #print("以%d做LR型调整" %(p.key))
                    p=self.LR(p)                #若结点p的左孩子的右子树较高,做LR型调整
                else:
                    #print("以%d做LL型调整" %(p.key))
                    p=self.LL(p)                #若结点p的左孩子的左子树较高,做LL型调整
        p.ht=max(self.getht(p.lchild),self.getht(p.rchild))+1   #更新结点p的高度
        return p

    def search(self,k):					     	#在AVL树中查找关键字为k的结点
        return self._search(self.r,k)			#r为AVL树的根结点

    def _search(self,p,k):	                    #被search方法调用
        if p==None: return None					#空树返回Nonel
        if p.key==k: return p.data		        #找到后返回p.data
        if k<p.key:
            return self._search(p.lchild,k)	    #在左子树中递归查找
        else:
            return self._search(p.rchild,k)	    #在右子树中递归查找

    def inorder(self):                          #中序遍历所有结点
        global res
        res=[]
        self._inorder(self.r)
        return res

    def _inorder(self,p):                       #被inorder方法调用
        global res
        if p!=None:
            self._inorder(p.lchild)
            res.append([p.key,p.data])
            self._inorder(p.rchild)
    
    def DispAVL(self):						        #输出AVL树的括号表示串
        self._DispAVL(self.r)

    def _DispAVL(self,p):           			    #被DispAVL方法调用
        if p!=None:
            print(p.key,end='')     			    #输出根结点值
            if p.lchild!=None or p.rchild!=None:
                print("(",end='')   			    #有孩子结点时才输出“(”
                self._DispAVL(p.lchild)			    #递归处理左子树
                if p.rchild!=None:
                    print(",",end='')   		    #有右孩子结点时才输出“,”
                self._DispAVL(p.rchild)			    #递归处理右子树
                print(")",end='')   			    #有孩子结点时才输出“)”

#主程序
if __name__ == '__main__':
    a=[1,2,5,4,1,2,5]
    print("(1)建立dic")
    dic=Dict()										#定义Dict对象dic
    for i in range(len(a)):
        if a[i] in dic:             					#若a[i]已存在，次数增1
            dic[a[i]]+=1
        else:                       				#若a[i]不存在，次数置为1
            dic[a[i]]=1
    print("(2)输出所有的元素：",dic.inorder())
    k=2
    print("(3)删除关键字%d" %(k))
    dic.delete(2)
    print("(4)删除后所有元素：",dic.inorder())

'''
#主程序
if __name__ == '__main__':
    a=[[16,"s16"],[3,"s3"],[7,"s7"],[11,"s11"],[9,"s9"],[26,"s26"],[18,"s18"],[14,"s14"],[15,"s15"]]
    bt=AVLTree()
    print("(1)创建AVL")
    for i in range(len(a)):
        print("插入%d\t" %(a[i][0]),end='')
        bt.insert(a[i][0],a[i][1])
        print("AVL:",end=' ')
        bt.DispAVL(); print()
    b=[11,9,3]
    print("(2)删除操作")
    for i in range(len(b)):
        print("删除%d\t" %(b[i]),end='')
        bt.delete(b[i])
        print("AVL:",end=' ')
        bt.DispAVL(); print()
'''    