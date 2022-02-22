lst=eval(input())
n,m=eval(input())
a=len(lst)
k=0
if n<m:
    if a<m:
        print("error")
        quit()
if m<n:
    k=1
    if a<n:
        print("error")
        quit()
if(k==1):
    k=n
    n=m
    m=k
for x in range(m,n,-1):
    del lst[x]
print(lst)