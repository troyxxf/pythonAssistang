lis1=eval(input())
lis2=[]
for x in lis1:
    flag=0
    for j in range(2,x-1):
        if x%j==0:
            flag=1
            break
    if flag==0:
        lis2.append(x)
print(lis2)

