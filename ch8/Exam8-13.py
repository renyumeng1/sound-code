from AVL import AVLTree
class Dict:
    def __init__(self):             #构造方法
        self.avl=AVLTree()

    def insert(self,k,d):           #插入(k,d)
        self.avl.insert(k,d)

    def delete(self,k):             #删除k
        self.avl.delete(k)

    def inorder(self):              #按关键字递增输出所有元素
        return self.avl.inorder()

    def __contains__(self,k):       #in运算符重载
        if self.avl.search(k)!=None:
            return True
        else:
            return False

    def __getitem__(self,k):        #按关键字取值
        return self.avl.search(k)
    
    def __setitem__(self,k,d):      #按关键字赋值
        self.avl.insert(k,d)
        
        
#主程序
if __name__ == '__main__':
    a=[1,2,5,4,1,2,5]
    print("(1)建立dic")
    dic=Dict()
    for i in range(len(a)):
        if a[i] in dic:             #若a[i]已存在，次数增1
            dic[a[i]]+=1
        else:                       #若a[i]不存在，次数置为1
            dic[a[i]]=1
    print("(2)输出所有的元素：",dic.inorder())
    k=2
    print("(3)删除关键字%d" %(k))
    dic.delete(2)
    print("(4)删除后所有元素：",dic.inorder())
     
