n = input().split(' ')
m = input().split(' ')
k = input().split(' ')
a = {"name":"Zhang","english":80,"python":90,"math":100}
b = {"name":"Zhang","english":80,"python":90,"math":100}
c = {"name":"Zhang","english":80,"python":90,"math":100}
a["name"] = n[0]
a["english"] = eval(n[1])
a["python"] = eval(n[2])
a["math"] = eval(n[3])
a["avg"] = round((eval(n[1])+eval(n[2])+eval(n[3]))/3,2)
b["name"] = m[0]
b["english"] = eval(m[1])
b["python"] = eval(m[2])
b["math"] = eval(m[3])
b["avg"] = round((eval(m[1])+eval(m[2])+eval(m[3]))/3,2)
c["name"] = k[0]
c["english"] = eval(k[1])
c["python"] = eval(k[2])
c["math"] = eval(k[3])
c["avg"] = round((eval(k[1])+eval(k[2])+eval(k[3]))/3,2)
z = []
z.append(a)
z.append(b)
z.append(c)
z.sort(key=lambda x:x['avg'])
print(z)