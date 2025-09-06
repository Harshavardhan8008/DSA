def solve(A):
    L = []
    for columns in range(len(A[0])):
        sumT=0
        for rows in range(len(A)):
            print(A[rows][columns])
            sumT+=sumT+A[rows][columns]
        L.append(sumT) 
    return L         
A=[[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]

solve(A)