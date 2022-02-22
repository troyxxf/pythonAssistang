a=input()
for i in range(len(a)):
    while a.count(a[i])>1:
        a.remove(a[i])
print(a)