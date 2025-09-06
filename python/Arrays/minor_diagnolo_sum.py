def solve(A):
    sumT=0
    for row in range(len(A)):
        for column in range(len(A[row])):
            if(row+column +2 == len(A) + 1):
                sumT+=A[row][column]
                print(sumT)    
    return sumT 
A = [[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]] 

solve(A)