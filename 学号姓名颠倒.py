lst=["20190001张三","20190002李四","20190005王五"]
for x in range(len(lst)):
    lst[x]=lst[x][-2:]+lst[x][:8]
print(lst)