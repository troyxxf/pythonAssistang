lis1=eval(input())
lis2=[]
for x in lis1:
    if x==2:
        lis2.append(x)
    elif x%2==0:
        break
    else:
        lis3=[j for j in range(3,x)]
        for i in lis3:
            if x%i==0:
                break
            if i==(x-1):
                lis2.append(x)
print(lis2)