  # @return a list of list of integers            
def solve(A):
    def printArray(Array,index1,index2):
        listResult = []
        for i in range(index1,index2+1):
            listResult.append(Array[i])
        return listResult 
    i=0
    j=0
    result = []
    while(i<len(A)):
        while(j<len(A)):
            resultArray = printArray(A,i,j)
            result.append(resultArray)
            j+=1
        i+=1
        j=i
    print(len(result))    
    return result  

A=[36,63,63,26,87,28,77,93,7]
print(solve(A))