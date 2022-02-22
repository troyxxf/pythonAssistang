a = input()
b = input()
la = len(a)
lb = len(b)
#建立二维列表，行数la+1，列数lb+1,初值为0
res = [[0 for i in range(lb+1)]  for j in range(la+1)]
print(res)
lc = []
mmax = 0
for i in range(1, la+1):
   for j in range(1, lb+1):
      if a[i-1] == b[j-1]:
         res[i][j] = res[i-1][j-1] + 1
         if(mmax<res[i][j]):
            mmax = res[i][j]
            lc.append(a[i-1])
print(mmax)
print(''.join(lc))

