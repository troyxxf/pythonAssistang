# dic={('a',1),('b',2),('c',3)}
# for i in dic:
#     for j in i:
#         print("{:10}".format(j),end="")
#     print()
employee = {"0001":"Mary","St0002":"Lee","D0003":"Wang"}
lst=[('St0002-Shanghai', 11), ('0001-Chongqing', 5), ('D0003-Nanjing', 4)]
l=[]
for i in range(3):
    l.append(lst[i][0])
l1=l.copy()
l2=[]
l3=[]
for x in range(len(lst)):
    l1[x]=list(l1[x])
    p=l1[x].index('-')
    n1=l[x][0:p]
    n2=l[x][p+1:len(l1[x])]
    l2.append(n1)
    l3.append(n2)
for x in range(len(lst)):
    print("{:<10s}{:<10s}{:<10}".format(l3[x],employee[l2[x]],lst[x][1]))
#print(l3[x],employee[l2[x]],lst[x][1])（像这样可以输出）