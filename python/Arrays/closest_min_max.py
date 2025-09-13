def solve(A):
    resultIndex = float('inf')
    maximum = max(A)
    minIndex = None
    maxIndex = None
    minimum = min(A)
    print(minimum,maximum)
    for i in range(len(A)):
        if(A[i]==minimum):
            minIndex = i
        if(A[i]==maximum):
            maxIndex = i 
        if(maxIndex is not None and minIndex is not None):
            print(minIndex,maxIndex)
            resultIndex = min(resultIndex,abs(maxIndex-minIndex))
    return resultIndex + 1   
A=[834,563,606,221,165]  
print(solve(A))