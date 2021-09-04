def Min(a,i):                   #求a[0..i]中的最小值
    if i==0:					#递归出口
        return a[0]
    else:						#递归体
        min=Min(a,i-1)
        if (min>a[i]): return a[i]
        else: return min

a=[3,2,1,5,4]
print(Min(a,4))