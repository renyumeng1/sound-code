def pow(x,n):               #求x的n次幂
    if n==1:
        return x;
    p=pow(x,n//2)
    if n%2==1:
        return x*p*p	    #n为奇数
    else:
        return p*p			#n为偶数

x=2.0
n=5
print(pow(x,n))

