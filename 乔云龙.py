lst1=list()
lst2=list()
x=eval(input())
lst=[int(x[i]) for i in range (len(x))]
a=len(lst)
for i in range(a):
    if lst[i]!=0:
        lst1.append(lst[i])
    if lst[i]==0:
        lst2.append(lst[i])
lst1.extend(lst2)
print(lst1)