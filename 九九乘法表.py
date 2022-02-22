n=eval(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print("%d*%d=%d"%(i,j,(i*j)))
            break
        print("%d*%d=%d"%(i,j,(i*j)),end=" ")