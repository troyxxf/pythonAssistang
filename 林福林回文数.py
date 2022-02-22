a=eval(input())
def huiwen(x):
    x1=str(x)
    if x1==x1[::-1]:
        return True
    else:
        return False
def sushu(x):
    if x==2:
        return True
    if x>2:
        for y in range(2,int(x**0.5+1)): #此处缩小了便遍历范围
            if x%y==0:
                return False
        return True
i=0
j=2
while i<a:
    if huiwen(j)==True and sushu(j)==True:
        i+=1
        if i%10 !=0:
            print('%6d'%j,end='')
        else:
            print('%6d'%j)
    j+=1