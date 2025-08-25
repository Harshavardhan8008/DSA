def solve(A):
    if(len(A)==1):
        return -1
    for i in range(len(A)-1):
        B = sorted(A,reverse=True)
        if(B[i]==B[i+1]):
            continue
        else:
            return B[i+1]
    return -1            