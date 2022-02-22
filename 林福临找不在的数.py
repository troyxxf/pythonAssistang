nums=eval(input())
def missNumber(nums):
   # number=0
    for x in range(0,len(nums)+1):
        if nums.count(x)!=1:
            number=x
    return number
number = missNumber(nums)
print(number)