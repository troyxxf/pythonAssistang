lst=input().split()
#上面这句会把你的输入存为列表
print(lst)#输出给你看
sum=0
for x in lst:#这个x就是列表中的每一个值
    sum+=int(x)#因为列表中的元素还是字符串，只有数值类型才能相加，所以变为int
print(sum)