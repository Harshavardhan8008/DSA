def solve(A):
    Lrow=[]
    Lcol = []
    for row in range(len(A)):
        for col in range(len(A[row])):
            if(A[row][col]==0):
                Lcol.append(col)
                Lrow.append(row)
    for row in range(len(A)):
        for column in range(len(A[row])):
            if(row in Lrow):
                A[row][column] = 0
            if(column in Lcol):
                A[row][column] =0
    return A                          
      


A=[[1,2,3,4],
[5,6,7,0],
[9,2,0,4]]
print(solve(A))