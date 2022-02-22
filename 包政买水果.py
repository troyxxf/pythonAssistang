a=input()
b={}
while a!="None":
    a=a.split()
    if "a[0]" not in b.keys():
        b[a[0]]=[1,eval(a[1])]
    else:
        b[a[0]][0]+=1
        b[a[0]][1]+=eval(a[1])
    a=input()
c=sorted(b.items(),key=lambda x:(-x[1][1],-x[1][0],x[0]))
for i in range(len(c)):
    print(c[0],c[1][0],c[1][1])