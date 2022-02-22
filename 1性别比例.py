
lst=eval(input())
m,n=eval(input())
c=len(lst)

if m>c-1 or n>c-1 or m<0 or n<0:
    print("error")
elif m<n:
    del lst[m:n]
    print(lst)
elif m>n:
    del lst[m:n:-1]
    print(lst)
