n=99999
b=eval(input())
a=[]
c=0
if n<0 or n%1!=0:
    print("illegal input")
else:
    for h in range(2,n+1):
        if str(h)==str(h)[::-1]:
            for i in range(2,h):
                if h%i==0:
                    break
            else:
                a.append(int(h))
        else:
            pass
for i in range(b):
    c+=1
    if c%10==0:
        print("{:6}".format(a[i]))
    else:
        print("{:6}".format(a[i]),end="")
    
    