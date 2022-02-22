n,m=map(eval(input()).split(" "))
if(m-n>=3 and n>=0 and m<11):
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):#为什么a是个位呢
                if a!=b and b!=c and c!=a and c!=0:
                    print(a*100+b*10+c)        
else:
    print("illegal input")