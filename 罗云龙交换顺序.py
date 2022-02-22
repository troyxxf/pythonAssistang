s=eval(input())
n,m=input().split(',')
m=int(m)
n=int(n)
if(-len(s)<m<len(s)-1 and -len(s)<n<len(s)-1):
    if m<n:
        q=m
        m=n
        n=q
        lst1=[]
        for i in range(n):
            lst1.append(s[n])
        lst2=s[m:]
        lst2.extend(lst1)    
        print(lst1)
    else:
        lst1=[]
        for i in range(n):
            lst1.append(s[n])
        lst2=s[m:]
        lst2.extend(lst1)    
        print(lst1)
else:
	print("error")