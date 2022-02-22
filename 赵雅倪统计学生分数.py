score=[]
for i in range(3):
    stu={}
    stu["name"],stu["english"],stu["python"],stu["math"]=input().split(" ")
    score.append(stu)
for i in range(3):
    avg=(int(score[i]["english"])+int(score[i]["python"])+int(score[i]["math"]))/3.0
    avg=round(avg,2)
    score[i]["avg"]=avg
print(score)