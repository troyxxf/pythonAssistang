def printMatrix(matrix):
    result=[]
    # write code here
    for i in range (len(matrix[0])):
        result.append(matrix[0][i])
    matrix.remove(matrix[0])
    for j in range(len(matrix)):
        result.append(matrix[j][len(matrix[j])-1])
        matrix[j].remove(matrix[j][len(matrix[j])-1])
    for i in range(len(matrix[len(matrix)-1])):
        result.append(matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1-i])
    matrix.remove(matrix[len(matrix)-1])
    for j in range(len(matrix)):
        result.append(matrix[len(matrix)-1-j][0])
        matrix[len(matrix)-1-j].remove(matrix[len(matrix)-1-j][0])
    if(len(matrix)!=0):
        result=result+printMatrix(matrix)
    return result

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(printMatrix(matrix))