def job(time):
    time_job={}
    time_job['A']=time[0]
    time_job['B']=time[1]
    time_job['C']=time[2]
    time_list={}
    for x in time_job.keys():
        for y in time_job.keys():
            if x!=y:
                for z in time_job.keys():
                    if z!=x and z!=y:
                        time_list[x+y+z]=time_job[x][0]+time_job[y][1]+time_job[z][2]
    time_arrange=list(time_list.items())
    time_arrange.sort(key=lambda x:x[1])
    return time_arrange[0][::-1]
time_all=[]
for x in range(3):#读3行                
    time_one=input().split()
    time_one=[eval(x)  for  x  in  time_one]
    time_all.append(time_one)
result=job(time_all)
for x in result:
    print(x,end=" ")