GDP={}
stringA=input()
while stringA!="ok":
    lst=stringA.split()#变成列表而且分隔的字符
    GDP[lst[0]]=eval(lst[1])#数值的话 都要记得加eval 字典中如何添加键值对
    stringA=input()#不写的话无法继续执行

GDP['China']=95
del GDP['Japan']
print(len(GDP),GDP['USA'])
