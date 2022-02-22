def level(mylist):
    if  isinstance(mylist,list):
        if len(mylist)==0:
            return 1
        a=[]
        for i in mylist:
            a.append(level(i))
            print(a)
        max_level=max(a)
        return  max_level+1
    else:
        return 0
origin=eval(input())
print(level(origin))