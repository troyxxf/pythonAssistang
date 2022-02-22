s=input()
if len(s)!=18:
    print("Error")
else:
    s1=s[:len(s)-1]
    lst2=list(s1)
    lst2=[eval(x) for x in lst2] #['5', '3', '0', '1', '0', '2', '1', '9', '2', '0', '0', '5', '0', '8', '0', '1', '1']
    lst3=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    lst4=[]
    lst5=[1,0,'X',9,8,7,6,5,4,3,2]
    for x in range(len(lst2)):
        p=lst2[x]*lst3[x]
        lst4.append(p)
    q1=sum(lst4)
    n=q1%11
    zuihou=lst5[n]
    if zuihou==lst2[len(lst2)-1]:
        print("Correct")
    else:
        print("Wrong")
