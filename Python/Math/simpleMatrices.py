matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[9,8,7],[6,5,4],[3,2,1]]
matrix3 = [[3,2,1],[6,5,4],[9,8,7]]

def AddMatrices(A, B):
    size = len(A)
    C = []
    for row in range(size):
        curRow = []
        for col in range(size):
            curRow.append(A[row][col] + B[row][col])
        C.append(curRow)
    return C

def printMatrix(matrix, label):
    print(label + ":")
    for row in matrix:
        print(row)
    print("")
        
printMatrix(AddMatrices(matrix1,matrix2), "Example1")
printMatrix(AddMatrices(matrix1,matrix3), "Example2")
printMatrix(AddMatrices(matrix2,matrix3), "Example3")