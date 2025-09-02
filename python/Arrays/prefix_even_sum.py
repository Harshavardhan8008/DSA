def sumOfEvenIndexedElements(A, B):
    preSum = [i for i in range(len(A))]
    result = []
    for i in range(len(A)):
        if(i==0):
            preSum[0] = A[i]
        elif(i%2==0):
            preSum[i] = preSum[i-1] + A[i]
        else:
            preSum[i] = preSum[i-1]   
    for i in range(len(B)): 
        if(B[i][0]==0):
            result.append(preSum[B[i][1]])
        else:
            result.append(preSum[B[i][1]] - preSum[B[i][0]-1])
    return result                     
    
A=[2,8,3,9,15]
B = [ [1, 4], 
      [0, 2], 
      [2, 3] ]
print(sumOfEvenIndexedElements(A,B))