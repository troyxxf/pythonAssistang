import math
import pandas as pd
# lst=[55.0, 58.7, 59.7, 61.2, 62.5, 64.5, 65.8, 66.5, 67.0, 70.5, 71.0, 77.0, 80.2, 89.5]
lst=[]
n=eval(input())
while n!=0:
    lst.append(n)
    n=eval(input())
junzhi=sum(lst)/len(lst)
print("均值:",junzhi)
print("length",len(lst))
fangcha_sun=0.0
for i in range(len(lst)):
    fangcha_sun+=(lst[i]-junzhi)**2
fangcha=fangcha_sun/len(lst)
print("方差:",fangcha)
biaozhuncha=math.sqrt(fangcha)
print("标准差：",biaozhuncha)
s = pd.Series(lst)
print("偏度：",s.skew())
print("峰度：",s.kurt())

f1u_sum=0
for i in lst:
    f1u_sum+=(i-junzhi)**4
f1u=f1u_sum/len(lst)
f1d=fangcha**2
fengdu=f1u/f1d
print("自己算峰度：",fengdu)

p1u_sum=0
for i in lst:
    p1u_sum+=(i-junzhi)**3
p1u=p1u_sum/len(lst)
p1d=biaozhuncha**3
piandu=p1u/p1d
print("自己算偏度:",piandu)