def sumlist(lst):
    lst1=[]
    for x in lst:
        if(type(x)==int):
            lst1.append(x)
        else:
            lst1.append(sumlist(x))
    return sum(lst1)

lst=eval(input())
print(sumlist(lst))