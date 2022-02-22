lis=list(input().split(" "))
lis1=[]
for x in lis:
    x=int(x)
    n=(x+5)%10
    lis1.append(n)
lis1.reverse()
b=[str(i) for i in lis1]
c=(''.join(b))
print(c)