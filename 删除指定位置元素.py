s=eval(input())
m,n=input().split(',')
m=int(m)
n=int(n)
lst1=s[0:m]
lst2=s[n:]
lst1.extend(lst2)
print(lst1)