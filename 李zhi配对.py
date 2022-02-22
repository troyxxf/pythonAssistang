def main():
    somestr,substr,startstr,endstr=input().split()
    startnum=int(startstr)
    endnum=int(endstr)
    fun(somestr, substr, startnum, endnum)

def fun(somestr,  substr,  startnum,  endnum):
    ls=[]
    for i in range(startnum,endnum-1):
        if somestr[i]==substr[0] and somestr[i+1]==substr[1] and somestr[i+2]==substr[2]:
            ls.append(i)
    if len(ls)==0:
        print("none")
    else:
        for x in ls:
            x=[str(y) for y in ls]
        print(",".join(x))


main()




