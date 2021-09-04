def Level(t,i):                     #求t中索引i的结点的层次
    assert i>=0 and i<len(t)        #检测参数
    cnt=1
    while t[i][1]!=-1:              #没有到达根结点时循环
        cnt+=1
        i=t[i][1]                   #移动到双亲结点
    return cnt
        
t=[['A',-1], ['B',0], ['C',0], ['D',1], ['E',1], ['F',1], ['G',4]]
print(Level(t,5))
