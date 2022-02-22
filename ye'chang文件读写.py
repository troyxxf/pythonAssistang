with open('in.txt','r') as f:
    str1=f.readline()
    lst=str1.split()
    dic={}
print(lst)
for x in lst:
    dic[x]=lst.count(x)
print(dic)
l1=list(dic.items())
print(l1)
l1.sort(key=lambda k:(-k[1],k[0]))
print(l1)
for i in range(len(l1)):
    with open('out1.txt','a') as d:
        d.write(str(l1[i][0])+str(l1[i][1]))