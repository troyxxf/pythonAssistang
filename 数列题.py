#举个例子，求【1/2，2/3，3/4，4/5.......】
#输入n
#输出列表中前n个元素的和
lst=[]
n=eval(input())
for i in range(n):
    lst.append((i+1)/(i+2))
result=sum(lst)
print("%.4f"%result)