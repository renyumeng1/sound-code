from SqString import SqString
def Strcmp(s,t):
    minl=min(s.getsize(),t.getsize())   #求s和t中最小长度
    for i in range(minl):				#在共同长度内逐个字符比较
        if s[i]>t[i]:
            return 1
        elif s[i]<t[i]:
            return -1
    if s.getsize()==t.getsize():		#s==t
        return 0
    elif s.getsize()>t.getsize():		#s>t
        return 1
    else:  return -1					#s<t

cstr1="abcd1"
s1=SqString()
s1.StrAssign(cstr1)
print("s1: ",end='');s1.DispStr()
    
cstr2="abcd"
s2=SqString()
s2.StrAssign(cstr2)
print("s2: ",end='');s2.DispStr()
print(Strcmp(s1,s2)) 



