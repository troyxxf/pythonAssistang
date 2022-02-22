m=[]
n=[]
p=[]
for i in range(3):
    a,b,c,d=input().split( )
    b=int(b)
    c=int(c)
    d=int(d)
    s=[('name',a),('englishi',b),('python',c),('math',d)]
    e=float((b+c+d)/3)
    n.append(e)
    s.append(('avg',round(e,2)))
    f=dict(s)
    m.append(f)
print(n)
for x in range(3):
    # print(m)
    flag=0
    h=max(n)
    for i in range(len(m)):
        if m[i]['avg']==h:
            print(m[i]['avg'])
            p.append(m[i])
            n.remove(max(n))
            # print(n)
print(p)
