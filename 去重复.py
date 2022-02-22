str1=input()
lst=eval(str1)
for x in lst:
    k=lst.count(x)
    if k>1:
        # for y in range(k):
        #     lst.remove(x)
        #     print(lst,"test")
print(lst)