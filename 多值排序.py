lst=[[1,2],[1,3],[3,2],[3,3],[2,2],[2,3]]
lst.sort(key=lambda x:(-x[0],x[1]))
print(lst)