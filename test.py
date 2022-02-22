n=123
sum1=0
while(n>=1):
    sum1+=n%10
    n='%d'%(n/10)
print(sum1)