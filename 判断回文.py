def huiwen(i):
    n=str(i)
    m=n[::-1]
    if n==m:
        return 1
    else:
        return 0
num=121
print(huiwen(num))