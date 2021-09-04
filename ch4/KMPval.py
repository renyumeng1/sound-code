from SqString import SqString
MaxSize=100
def GetNextval(t,nextval):      #由模式串t求出nextval值
    j,k=0,-1
    nextval[0]=-1
    while j<t.getsize()-1:
        if k==-1 or t[j]==t[k]:
            j,k=j+1,k+1
            if t[j]!=t[k]:
                nextval[j]=k
            else:
                nextval[j]=nextval[k]
        else: k=nextval[k]

def KMPval(s,t):                       #改进后的KMP算法
    nextval=[None]*MaxSize
    GetNextval(t,nextval)				    #求nextval数组
    i,j=0,0
    while i<s.getsize() and j<t.getsize():
        if j==-1 or s[i]==t[j]:
            i,j=i+1,j+1             #i,j各增1
        else: j=nextval[j] 		    #i不变,j回退
    if j>=t.getsize():
        return(i-t.getsize())	    #返回起始序号
    else:
        return(-1)					#返回-1

if __name__ == '__main__':
    cstr1="aaaaab"
    s=SqString()
    s.StrAssign(cstr1)
    print("s: ",end='');s.DispStr()
    
    cstr2="aaab"
    t=SqString()
    t.StrAssign(cstr2)
    print("t: ",end='');t.DispStr()

    print("BF: %d" %(KMPval(s,t)))



