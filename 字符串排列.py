def Permutation(ss):
    result=[]
    # write code here
    for i in range(len(ss)):
        result.append(ss[i]+Permutation(ss.remove(ss[i])))
    return result

ss="ab"
print(Permutation(ss))