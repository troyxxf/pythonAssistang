def Fibonacci(num,n):
    x=num[0]
    y=num[1]
    for i in range(2,n):
        num.append(num[i-1]+num[i-2])
    return num[n-1]
num=[1,1]
n=int(input())
print(Fibonacci(num,n))