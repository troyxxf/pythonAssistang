lst=eval(input())
n,m=eval(input())
n,m=int(n),int(m)
x=len(lst)
if m>=x or n>=x:
    print("error")
else:
    temp=lst[m]
    lst[m]=lst[n]
    lst[n]=temp
    print(lst)