d={}
s=input()
with open("in.txt",'w') as f:
    f.write(s)
f.close()
with open('in.txt','r') as f:
    info=f.read().split()
for x in info:
    d[x]=d.get(x,0)+1
ls=list(d.items())
ls.sort(key=lambda x:(-x[1],x[0]))
#print(ls)
with open("out.txt",'w') as f:
    for x in range(len(ls)):
        f.write(ls[x][0]+" "+str(ls[x][1])+"\n")
lst=[]
with open("out.txt",'r') as f:
    lst=f.read().split()
for x in range(0,len(lst),2):
    print(lst[x],lst[x+1])
        


