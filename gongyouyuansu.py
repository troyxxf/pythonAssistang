lst1=eval(input())
lst2=eval(input())
lst3=[]
for x,y in zip(lst1,lst2):
    if x==y:
        pass
    else:
        lst3.append(x)
        # print(x)
lst3.sort()
lst4=[]
[lst4.append(i) for i in lst3 if not i in lst4]
print(lst4)