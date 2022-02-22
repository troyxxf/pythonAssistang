def isprime(i):
    if i>1:
        for s in range(2,i):
            if i%s==0:
                return 0
                break
        return 1
def reversenumber(i):
    num=str(i)
    m=num[::-1]
    if num==m:
        return 1
    else:
        return 0
n=eval(input())
i=2
count=1
while count<n+1:
    if reversenumber(i)==1 and isprime(i)==1:
        if count%10==0:
            # print("\n")
            print("{:6}".format(i))
        else:
            print("{:6}".format(i),end=" ")
        count+=1
    i=i+1
