def maxsum(nums):
    nums=sorted(nums)
    # print(nums)
    nums1=nums[0::2]
    # print(nums1)
    maxsum=0
    for x in nums1:
        maxsum+=x
    return maxsum
nums=eval(input())
v=maxsum(nums)
print(v)