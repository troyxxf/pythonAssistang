def sumlist(nums):
    a=list(nums)
    # b=[]
    sumv=0
    c=0
    for i in range(len(a)):
        if type(a[i]) is int:
            sumv+=a[i]
        #     b.append(a[i])
        # elif type(a[i]) is list:
        else:
            sumv+=sumlist(a[i])
        # sumv=sum(a[i])+c
    return sumv
nums  =  eval(input())
sumv  =  sumlist(nums)
print(sumv)