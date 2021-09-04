class BSTNode:								        #二叉排序树结点类
    def __init__(self,k,d=None,l=None,r=None):      #构造方法
        self.key=k							        #存放关键字,假设关键字为int类型
        self.data=d                                 #存放数据项
        self.lchild=l						        #存放左孩子指针
        self.rchild=r						        #存放右孩子指针

class BSTClass:								        #二叉排序树类
    def __init__(self):                             #构造方法
        self.r=None  						        #二叉排序树根结点
        self.f=None    						        #用于存放待删除结点的双亲结点

    #二叉排序树的基本运算算法
    def InsertBST(self,k,d): 					    #插入一个(k,d)结点
        self.r=self._InsertBST(self.r,k,d)	

    def _InsertBST(self,p,k,d):           	        #在以p为根的BST中插入关键字为k的结点
        if p==None:							        #原树为空,新插入的元素为根结点
            p=BSTNode(k,d)
        elif k<p.key: 
            p.lchild=self._InsertBST(p.lchild,k,d)    #插入到p的左子树中
        elif k>p.key:
            p.rchild=self._InsertBST(p.rchild,k,d)    #插入到p的右子树中
        else:                                       #找到关键字为k的结点,修改data属性
            p.data=d
        return p

    def CreateBST(self,a):						    #由关键字序列a创建一棵二叉排序树
        self.r=BSTNode(a[0][0],a[0][1])				#创建根结点
        for i in range(1,len(a)):					#创建其他结点
            self._InsertBST(self.r,a[i][0],a[i][1])	#插入a[i]

    def SearchBST(self,k):					        #在二叉排序树中查找关键字为k的结点
        return self._SearchBST(self.r,k)			#r为二叉排序树的根结点

    def _SearchBST(self,p,k):	                    #被SearchBST方法调用
        if p==None: return None						#空树返回null
        if p.key==k: return p						#找到后返回p
        if k<p.key:
            return self._SearchBST(p.lchild,k)	    #在左子树中递归查找
        else:
            return self._SearchBST(p.rchild,k)	    #在右子树中递归查找

    def DeleteBST(self,k):					        #删除关键字为k的结点
        self.f=None
        return self._DeleteBST(self.r,k,-1)		    #r为二叉排序树的根结点

    def _DeleteBST(self,p,k,flag):	                #被DeleteBST方法调用
        if p==None:
            return False						    #空树返回False
        if p.key==k:
            return self.DeleteNode(p,self.f,flag)	#找到后删除p结点
        if k<p.key:
            self.f=p
            return self._DeleteBST(p.lchild,k,0)	#在左子树中递归查找
        else:
            self.f=p
            return self._DeleteBST(p.rchild,k,1)	#在右子树中递归查找

    def DeleteNode(self,p,f,flag):                  #删除结点p（其双亲为f）
        if p.rchild==None:						    #结点p只有左孩子(含p为叶子的情况)
            if flag==-1:						    #结点p的双亲为空(p为根结点)
                self.r=p.lchild						#修改根结点r为p的左孩子
            elif flag==0:							#p为双亲f的左孩子
                self.f.lchild=p.lchild				#将f的左孩子置为p的左孩子
            else:									#p为双亲f的右孩子
                self.f.rchild=p.lchild				#将f的右孩子置为p的左孩子
        elif p.lchild==None:					    #结点p只有右孩子
            if flag==-1:						    #结点p的双亲为空(p为根结点)
                self.r=p.rchild					    #修改根结点r为p的右孩子
            elif flag==0:					        #p为双亲f的左孩子
                self.f.lchild=p.rchild			    #将f的左孩子置为p的左孩子
            else:									#p为双亲f的右孩子
                self.f.rchild=p.rchild				#将f的右孩子置为p的左孩子
        else:                            			#结点p有左右孩子
            f1=p 								    #f1为结点q的双亲结点
            q=p.lchild             		            #q转向结点p的左孩子
            if q.rchild==None:						#若结点q没有右孩子
                p.key=q.key							#将被删结点p的值用q的值替代
                p.data=q.data
                p.lchild=q.lchild					#删除结点q
            else:									#若结点q有右孩子
                while q.rchild!=None:   			#找到最右下结点q,其双亲结点为f1
                    f1=q
                    q=q.rchild
                p.key=q.key							#将被删结点p的值用q的值替代
                p.data=q.data
                f1.rchild=q.lchild					#删除结点q
        return True

    def DispBST(self):						        #输出二叉排序树的括号表示串
        self._DispBST(self.r)

    def _DispBST(self,p):           			    #被DispBST方法调用
        if p!=None:
            print(p.key,end='')     			    #输出根结点值
            if p.lchild!=None or p.rchild!=None:
                print("(",end='')   			    #有孩子结点时才输出“(”
                self._DispBST(p.lchild)			    #递归处理左子树
                if p.rchild!=None:
                    print(",",end='')   		    #有右孩子结点时才输出“,”
                self._DispBST(p.rchild)			    #递归处理右子树
                print(")",end='')   			    #有孩子结点时才输出“)”


#主程序
if __name__ == '__main__':
    #a=[[3,"s3"],[5,"s5"],[6,"s6"],[2,"s2"],[4,"s4"],[3,"s3"]]
    #a=[[5,None],[2,None],[1,None],[6,None],[7,None],[4,None],[3,None]]
    #a=[[1,None],[2,None],[3,None],[4,None],[5,None],[6,None],[7,None]]
    a=[[1,None],[1,None]]
    print("a: ",a)
    bt=BSTClass()
    print("创建BST")
    bt.CreateBST(a)
    print("BST:",end=' '); bt.DispBST(); print()
    print("插入10, BST:",end=' '); bt.InsertBST(10,"s10"); bt.DispBST();print()
    k=3
    print("查找%d的结果:%s" %(k,"成功" if bt.SearchBST(k) else "失败"))		
    print("删除4, BST:",end=' '); bt.DeleteBST(4); bt.DispBST(); print()
    print("删除3, BST:",end=' '); bt.DeleteBST(3); bt.DispBST(); print()
    print("删除1, BST:",end=' '); bt.DeleteBST(1); bt.DispBST(); print()
    print("删除2, BST:",end=' '); bt.DeleteBST(2); bt.DispBST(); print()
    print("删除20, BST:",end=' '); bt.DeleteBST(20); bt.DispBST(); print()
    print("删除5, BST:",end=' '); bt.DeleteBST(5); bt.DispBST(); print()
    print("删除6, BST:",end=' '); bt.DeleteBST(6); bt.DispBST(); print()
    print("删除10, BST:",end=' '); bt.DeleteBST(10); bt.DispBST(); print()