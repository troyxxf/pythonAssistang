n=int(input())
a=[]
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if i*i*i + j*j*j + k*k*k == 100*i + 10*j + k:
                m=100*i+10*j+k
                a.append(m)
flag=0
for x in range(len(a)):
    if a[x]<=n:
        flag=1
        print(a[x])
if flag==0:
    print("none")