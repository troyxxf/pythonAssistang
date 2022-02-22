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
y=[]
x.sort(key=lambda x:-x[1])
for i in x:
    a,b=i[0].split('-')
    if a=='0001':
        y.append([b,employee['0001'],i[1]])
    elif a=='st002':
        y.append([b,employee['st0002'],i[1]])
    else:
        y.append([b,employee['D0003'],i[1]])
for i in y:
    for j in i:
        print("{:10}".format(j),end="")
    print()