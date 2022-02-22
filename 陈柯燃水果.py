fruit={}
stringA = input()
while stringA!="None":
    lst = stringA.split() #列表被更新
    if lst[0] not in fruit:   #键
        fruit[lst[0]]=[1,eval(lst[1])]  #值是列表的形式
    else:
        fruit[lst[0]][0]+=1 #购买次数+1
        fruit[lst[0]][1]+=eval(lst[1]) #购买金额+1        
    stringA = input()
# lst1=sorted(fruit.items())
print(sorted(fruit.items))
lst1 = sorted(fruit ,key = lambda x:(-x[0][0],x[0][1])) 
dic = dict(lst1)
for k in dic:
    print(k,dic[k][0],dic[k][1])