s=input().split(' ')
m,n=input().split(' ')
m=int(m)
n=int(n)
if -len(s)<=m<=(len(s)-1) and -len(s)<=n<=(len(s)-1):
    k=s[m]
    s[m]=s[n]
    s[n]=k
    print(s)
else:
    print("error")