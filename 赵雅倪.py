c=input()
# c=c+" "
b=""
lis=[]
i=0
for x in c:
    print(x)
    b=b+x
    if x==" ":
        lis.append(b)
        b=""
lis.append(b)
print(lis)
lis.sort()
d={}
for i in lis:
    d[i]=lis.count(i)
m=max(d.values())
for k,v in d.items():
    if v==m:     
        print(k+"%d"%v)