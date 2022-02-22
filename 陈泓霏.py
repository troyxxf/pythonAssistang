string =input().split(" ")
s = []
num = 0
for x in range(len(string)):
    s.append(len(string[x]))
for i in s:
    num+=i
print("%d,%.2f"%(len(string),num/len(string)))