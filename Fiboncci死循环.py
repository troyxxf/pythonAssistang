def F(lst,m):
    m=int(m)
    if(m<0):
        return 0
    a=len(lst)
    if m<=a:
        return lst[m-1]
    else:
        # return int()
        return F(lst,m-1)+F(lst,m-2)
lst=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
m=eval(input())
print(F(lst,m))