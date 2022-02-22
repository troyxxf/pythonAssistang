n=eval(input())
lst=[x for x in range(1,n+1)]
print(lst)
ff=lst[0]
for y in range(len(lst)-1):
    lst[y]=lst[y+1]
    
    lst[len(lst)-1]=ff
    print(lst)
print(lst)