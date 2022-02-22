

def f(x):
    if x<20:
        y==6*x^2+1
    
    elif 20<=x<40:
        y==(3*x-60)^1/2
     
    else:
        y==100/(x+1)
    return y

x=eval(input())
result=f(x)
print("%.2f",result)