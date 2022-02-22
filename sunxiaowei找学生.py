stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
id=eval(input())
low=0
hight=len(stu_list)-1
while low<=hight:
    mid=(low+hight)//2
    if int(stu_list[mid][0])<id:
        low=mid+1
    elif int(stu_list[mid][0])>id:
        hight=mid-1
    else:
        a=''.join(stu_list[mid])
        print(a)
        break

else:
    print("None")