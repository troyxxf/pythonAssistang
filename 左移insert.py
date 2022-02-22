def list_move_left(A,a):
    for i in range(a):
        A.insert(len(A),A[0])
        A.remove(A[0])
    return A
A=[0,1,2,3,4,5]
a=2
B=list_move_left(A,a)
print(B)