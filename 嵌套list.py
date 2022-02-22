name=['a','b','c','d']
age=[1,2,3,4]
new=[]
for i in range(len(name)):
    littleOne=[]
    littleOne.append(name[i])
    littleOne.append(age[i])
    new.append(littleOne)
print(new)