def K_Small(A,B):
    C= sorted(A)
    return C[B-1]


print(K_Small([2,3,4,1,5,6],2))