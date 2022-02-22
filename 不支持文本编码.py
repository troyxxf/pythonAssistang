a=eval(input())
c=a
c.reverse()
print(c)
b=[]
for x in range(len(c)):
    if c[x] not in b:
        b.append(c[x])
    else:
        pass
b.reverse()
print(b)