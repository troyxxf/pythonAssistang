def ind(x,y):#此函数用于返回二位列表第一个下标
    for i in range(len(x)):
        if b[i][0]==y:
            return i
a=input()
b=[['I',1],['V',5],['X',10],['L',50],['C',100],['D',500],['M',1000]]
c=0
for i in range(len(a)):
    if i!=len(a)-1 and b[ind(b,a[i])][1]<b[ind(b,a[i+1])][1]:
        c-=b[i][1]
    else:
        c+=b[i][1]
print(c)