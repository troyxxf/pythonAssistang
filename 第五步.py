
list=input().split(",")
n,m=eval(input())
if -len(list)<=n<len(list):
    list=list+[list[n]]*m
    list=[eval(x) for x in list]
    print(list)
else:
    print("error")