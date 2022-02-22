x=input()
z=[]
i=0
while i<len(x):
    if i!=len(x)-1:
        if (x[i]=='I' and x[i+1]=='X') or (x[i]=='I' and x[i+1]=='V') or (x[i]=='X' and x[i+1]=='L') or (x[i]=='X' and x[i+1]=='C') or (x[i]=='C' and x[i]=='D') or (x[i]=='C' and x[i+1]=='M'):
            z.append(x[i]+x[i+1])
            i=i+2
        else:
            z.append(x[i])
            i=i+1
    else:
        z.append(x[i])
        i=i+1
q=0
for i in z:
    if i=='I':
        q=q+1
    if i=='V':
        q=q+5
    if i=='X':
        q=q+10
    if i=='L':
        q=q+50
    if i=='C':
        q=q+100
    if i=='D':
        q=q+500
    if i=='M':
        q=q+1000
    if i=='IV':
        q=q+4
    if i=='IX':
        q=q+9
    if i=='XL':
        q=q+40
    if i=='XC':
        q=q+90
    if i=='CD':
        q=q+400
    if i=='CM':
        q=q+900
print(q)