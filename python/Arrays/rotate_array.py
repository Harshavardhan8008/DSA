def Rotate(A, B):
    ListReturn =[0 for i in range(len(A))]
    for i in range(len(A)):
        index = (i+B)% len(A)
        ListReturn[index] = A[i]
        print(index)
    print(ListReturn)    
    return ListReturn   
A=[7,4,2,10,5]
B = 10
# A=[1,1,4,9,4,7,1]
# B = 9
Rotate(A,B)