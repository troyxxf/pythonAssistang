for i in range(3,100):
    flag=1
    for j in range(2,i//2):
        if i%j==0:
            #说明不是质数，标记变0
            flag=0
            break
    #标记还是1说明是质数
    if(flag==1):
        print(i)