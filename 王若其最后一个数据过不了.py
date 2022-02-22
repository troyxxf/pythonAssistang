def process(x,y,flag):
    total=0
    if flag<y:
        for i in x:
            if type(i)==list:
                flag=flag+1
                total=total+process(i,y,flag)
    else:
        print(x)
        total=len(x)
    return total
x=eval(input())
y=eval(input())
flag=1
result=process(x,y,flag)
if result==None:
    result=0
print(result)