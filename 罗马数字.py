lst = []
s = input()
i = 0
while i<len(s):
    if (i+1)<len(s) and s[i]=='I'and s[i+1]=='V': #判断有没有组合数的情况
        lst.append(4)
        i+=2                  #有组合数就跳过下一位 
    elif (i+1)<len(s) and s[i]=='I' and s[i+1]=='X':
        lst.append(9)
        i+=2
    elif (i+1)<len(s) and s[i]=='X' and s[i+1]=='L':
        lst.append(40)
        i+=2
    elif (i+1)<len(s) and s[i]=='X' and s[i+1]=='C':
        lst.append(90)
        i+=2
    elif (i+1)<len(s) and s[i]=='C' and s[i+1]=='D':
        lst.append(400)
        i+=2
    elif (i+1)<len(s) and s[i]=='C' and s[i+1]=='M':
        lst.append(900)  
        i+=2              
    else:  #当前不是组合数，则判断当前单数
        if s[i]=='I':
            lst.append(1)
            i+=1
        elif s[i]=='V':
            lst.append(5)
            i+=1
        elif s[i]=='X':
            lst.append(10)
            i+=1
        elif s[i]=='L':
            lst.append(50)
            i+=1
        elif s[i]=='C':
            lst.append(100)
            i+=1
        elif s[i]=='D':
            lst.append(500)
            i+=1                
        elif s[i]=='M':
            lst.append(1000)
            i+=1
            
print(sum(lst))