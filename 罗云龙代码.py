t0=eval(input())
t1=[]

l=len(t0)
for i in range(l):
    if t0[i]==2:
        t1.append(t0[i])
    else:
        for x in range(2,t0[i]):
            if t0[i]%x==0:
                break
            else:
                t1.append(t0[i])
print(t1)
x=[]
for i in t1:
    print(i)
    a=str(i)
    if a not in str(x):
        x.append(a)
print(x)