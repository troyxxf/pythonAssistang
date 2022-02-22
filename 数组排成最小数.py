def PrintMinNumber(numbers):
    # write code here
    result=10000000000
    if(len(numbers)==1):
        return int(numbers[0])
    for i in range(len(numbers)):
        for j in PrintMinNumber(numbers[:i]+numbers[i+1:]):
            temp=str(numbers[i])+str(j)
            print(temp)
            temp=int(temp)
            if(temp<result):
                result=temp
    return result

numbers=[4,3,2,1,5]
print(PrintMinNumber(numbers))