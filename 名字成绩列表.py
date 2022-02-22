
a=list(input().split(','))
b=eval(input())
d=[]
for i in range(len(a)):
    c=[]
    c.append(a[i])
    c.append(b[i])
    d.append(c)
print(d)