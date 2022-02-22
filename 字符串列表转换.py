lst=(input())
i=0
lst_copy=[]
for i in range(len(lst)):
    if(lst[i]=='['):
        flag=i
        continue
    if(lst[i]==','):
        lst_copy.append(lst[flag+1:i])
        flag=i
    if(lst[i]==']'):
        lst_copy.append(lst[flag+1:i])
print(lst_copy)