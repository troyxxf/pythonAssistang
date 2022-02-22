lst=eval(input())
lst1=[]
# lst2=[]
# lst3=[]
for x in range(len(lst)):
    k=lst.count(lst[x])
    if k>=1:
        if lst[x] not in lst1:
            lst1.append(lst[x])
    # else:
    #     lst2.append(lst[x])
# for x in range(len(lst)):
#     if lst[x] in lst1:
#         lst4=lst[x+1:len(lst)]
#         if lst[x] not in lst4:
#             lst3.append(lst[x])
# lst=lst3+lst2
print(lst1)