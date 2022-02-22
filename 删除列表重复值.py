lst=eval(input())
lst_copy=[]
for x in range(len(lst)):
    if lst[x:].count(lst[x])==1:
        lst_copy.append(lst[x])
print(lst_copy)