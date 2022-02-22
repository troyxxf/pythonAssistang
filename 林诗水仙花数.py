n=eval(input())
count=0
if n>1000:
    n=1000
for i in range(100,n+1):
    s=str(i)
    if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:#注意类型转换
        count+=1
        print(i)
if count==0:
    print('none')

