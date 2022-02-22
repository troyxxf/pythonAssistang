def sumlist(nums):
    lst1=[]
    for x in nums:
        if(type(x)==int):
            lst1.append(x)
        else:
            lst1.append(sumlist(x))
    sumv=sum(lst1)
    return sumv
nums  =  eval(input()) 
sumv  =  sumlist(nums) 
print(sumv)
