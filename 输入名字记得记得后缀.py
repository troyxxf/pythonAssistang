def f1(nums):
    print(nums)
    a=[]
    b=[]
    for x in nums:
        if x%2==1:
            a.append(x)
            # print(x)
        elif x%2==0:
            b.append(x)
            # print(x)
    # print(a)
    a.extend(b)
    # print(a)
    # print(c)
    return a
nums=[1,2,3,4,5]
print(f1(nums))