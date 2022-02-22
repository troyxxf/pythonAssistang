def  isPrime(n):
    a=0
    if n==2:
        return 1
    else:
        for i in range(2,n//2):
            if n%i==0:
                a=1
        if a==0:
            return 1
        else:
            return 0
def reverseNumber(n):
    a=str(n)
    x=a[::-1]
    return int(x)
N  =  int(input())
for  n  in  range(1,N+1):
        if  (isPrime(n)==1) and (reverseNumber(n)==n):
                print(n)