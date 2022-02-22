d={}
with open('in.txt','r') as f:
    info=f.read().split()
for x in info:
    d[x]=d.get(x,0)+1
ls=list(d.items())
ls.sort(key=lambda x:(-x[1],x[0]))
with open('out.txt','w') as f:
    for x in ls:
        f.write(x[0]+" "+str(ls.values())+"\n")