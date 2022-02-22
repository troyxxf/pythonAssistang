def F(num,n):
    a,b=1,1
    for i in range(2,n):
        a,b=b,a+b
        num.append(b)
    return num[n-1]
n=10
num=[1,1]
print(F(num,n))