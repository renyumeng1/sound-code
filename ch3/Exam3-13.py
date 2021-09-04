from LinkQueue import LinkQueue
def Jsequence(n,m):					#求约瑟夫序列
    qu=LinkQueue()                  #定义一个链队
    for i in range(1,n+1):          #进队编号为1到n的n个小孩
        qu.push(i)
    for i in range(1,n+1):			#共出列n个小孩
       	j=1
       	while j<=m-1:		    	#出队m-1个小孩，并将他们进队
            qu.push(qu.pop())
            j+=1
        x=qu.pop()                  #出队第m个小孩
        print(x,end=' ')
    print()
#主程序
print("测试1: n=6,m=3")
print("出列顺序:",end=' ')
Jsequence(6,3)
print("测试2: n=8,m=4")
print("出列顺序:",end=' ')
Jsequence(8,4)