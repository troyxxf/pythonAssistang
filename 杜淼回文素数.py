import math
def isPrime(num):
    if num==1:
        return False
    sqrt=int(math.sqrt(num))
    for j in range(2,sqrt+1):
        if num%j==0:
            return False
        else:
            # print(num)
            return True
def reverseNumber(num):
    n=str(num)
    m=n[::-1]
    return m
   


N = int(input())
for n in range(1,N+1):
    if reverseNumber(n)==n:
        print(n)
    if isPrime(n) and (reverseNumber(n) == str(n)):
        print(n) 