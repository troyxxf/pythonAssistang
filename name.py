list1=eval(input())
f=sum(list1)/len(list1)
if f%1==0 :
    print(int(f))
else:
    s="%.2f"%(f)
    print(s)