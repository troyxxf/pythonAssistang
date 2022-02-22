scores=[]
for i in range(3):
    s=input().split()
    stu={}    
    stu['name']=s[0]
    stu['english']=eval(s[1])
    stu['python']=eval(s[2])
    stu['math']=eval(s[3])
    scores.append(stu)
for i in range(len(scores)):
    avg=(scores[i]["english"]+scores[i]["python"]+scores[i]["math"])/3
    scores[i]["avg"]=round(avg,2)
scores.sort(key=lambda x:x["avg"],reverse=True)
print(scores)