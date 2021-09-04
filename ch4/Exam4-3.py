from LinkString import LinkString
def StrEqueal(s,t):
    if s.getsize()!=t.getsize():
        return False
    p=s.head.next
    q=t.head.next
    while p!=None and q!=None:
        if p.data!=q.data:
            return False
        p=p.next
        q=q.next
    return True;

cstr1="abcd"
s1=LinkString()
s1.StrAssign(cstr1)
print("s1: ",end='');s1.DispStr()
    
cstr2="abcd"
s2=LinkString()
s2.StrAssign(cstr2)
print("s2: ",end='');s2.DispStr()
print(StrEqueal(s1,s2)) 



