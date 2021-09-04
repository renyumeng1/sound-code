from LinkString import LinkString
def BF1(s,t):                       #链串的BF算法
    p=s.head.next			        #p指向s串的首结点
    i=0								#i为p指的首结点的序号为0
    while p!=None:
        p1=p;
        q=t.head.next			    #q指向t串的首结点
        while p1!=None and q!=None and p1.data==q.data:
            p1=p1.next			    #比较p1结点和q结点的字符,相等时同步后移
            q=q.next
        if q==None:return i			#t串比较完毕,返回i
        p=p.next;					#p移到s串的下一个结点
        i+=1
    return -1						#串t不是串s的子串时返回-1
if __name__ == '__main__':
    cstr1="aaaaab"
    s=LinkString()
    s.StrAssign(cstr1)
    print("s: ",end='');s.DispStr()
    
    cstr2="aaab"
    t=LinkString()
    t.StrAssign(cstr2)
    print("t: ",end='');t.DispStr()

    print("BF1: %d" %(BF1(s,t)))



