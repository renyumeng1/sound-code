from SqString import SqString
def BF(s,t):
    i,j=0,0
    while i<s.getsize() and  j<t.getsize():		#两串未遍历完时循环
        if s[i]==t[j]:			                #继续匹配下一个字符
            i,j=i+1,j+1							#目标串和模式串依次匹配下一个字符
        else:									#目标串、模式串指针回溯重新开始下一次匹配
            i,j=i-j+1,0							    #目标串从下一个位置开始匹配
    if j>=t.getsize():
        return (i-t.getsize())	                #返回匹配的第一个字符序号
    else:
        return (-1)							    #模式匹配不成功

if __name__ == '__main__':
    cstr1="aaaaab"
    s=SqString()
    s.StrAssign(cstr1)
    print("s: ",end='');s.DispStr()
    
    cstr2="aaab"
    t=SqString()
    t.StrAssign(cstr2)
    print("t: ",end='');t.DispStr()

    print("BF: %d" %(BF(s,t)))



