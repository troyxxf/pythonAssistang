stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
low=0
high=len(stu_list)-1
snum=int(input())
while low<=high:
    mid=(high+low)//2

    if snum>int(stu_list[mid][0]):
        low=mid+1
    elif snum<int(stu_list[mid][0]):
        high=mid-1
    else:
        a="".join(stu_list[mid])
        print(a)
        break
    if(mid==high or mid==low):
        break
else:
    print("None")