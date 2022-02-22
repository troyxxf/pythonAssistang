def prime(x):
    flag=0
    for i in range(2,x//2):
        if x%i==0:
            flag=1
            break
    if flag==0 or x==2:
        return True
    else:
        return False
def hw(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
n=eval(input())
count=0
x=2
while count<=n:
    if prime(x) and hw(x):
        count+=1
        if count%10!=0:
            print('%6d'%x,end='')
        else:
            print('%6d'%x)
    x+=1
