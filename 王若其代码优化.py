employee = {"0001":"Mary","St0002":"Lee","D0003":"Wang"}
i=eval(input())
x=[]
for q in range(i):
    a,b=input().split()
    x.append([a,int(b)])
y=[]
for i in range(len(x)):
    a=0
    for q in range(len(x)):
        if x[i][0]==x[q][0]:
            a=a+x[q][1]
    y.append([x[i][0],a])
x=[]
for i in y:
    if i in x:
        pass
    else:
        x.append(i)
print(x)
