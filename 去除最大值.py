lst=[5,4,1,5,5,5,2,3]
for x in lst:
    if((x==max(lst))or(x==min(lst))):
        lst.remove(x)
print(lst)