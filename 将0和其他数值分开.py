
list1=eval(input())
list2=[]
list3=[]
for x in list1:
    if x!=0:
        list2.append(x)
    else:
        list3.append(x)
    # if len(list2)<=len(list1):
    #     list2.append(0)
list1=list2+list3
print(list1)