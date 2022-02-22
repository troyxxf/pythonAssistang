list=eval(input())
list=[str(i) for i in list]
list.sort()
list.reverse()
b=int(''.join(list))
print(b)