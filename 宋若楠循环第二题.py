import string
i=0
sum=0
while 1:
    n=input()
    if n=='#':
        break
    i=i+1
    t=int(n)
    sum=sum+t
print('%d'%i,end=' ')
print('%d'%sum)