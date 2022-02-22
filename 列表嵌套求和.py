def sumlist(nums):
    p=0
    for i in nums:
        if type(i)==int:
            p=p+i
        else:
            p=p+sumlist(i)
            # p=p+i
    return p



nums = eval(input())
sumv = sumlist(nums)
print(sumv)