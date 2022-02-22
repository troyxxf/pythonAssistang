f = open("in.txt")
n = f.read()
f.close()

k = open("out.txt","a")

#n = input().split(' ')
n=n.split(' ')

m = {}
a = []
b = []

for x in n:
    m[x] = m.get(x,0)+1
#print(m)
for v,x in m.items():
    a.append(v)
    a.append(x)
    b.append(a)
    a = []
#print(b)
b = sorted(b,key = lambda x : (-x[1],x[0]))
c = []
q = ' '
for x in b:
    x[0] = str(x[0])
    x[1] = str(x[1])
    c.append(q.join(x))
#print(c)
k=open("out.txt","w")
for x in c:
    print(x)
    k.write(x)
k.close()