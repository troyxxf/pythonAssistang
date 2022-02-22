def f(a):
    b=[]
    p=[]
    for i in a:
        # print(i)
        if i=='[ ' or i=='(' or i=='{':
            # print(b)
            b.append(i)
            print(b)
        elif i==']':
            print(b)
            if len(b)==0 or b.pop()!='[':
                print(b)
                return False
        elif i==')':
            if len(b)==0 or b.pop() !='(':
                return False
        elif i=='}':
            if len(b)==0 or b.pop() !='{':
                return False
    if len(b)==0:
        return True
    else:
        return False

a=list(input())
print(f(a))