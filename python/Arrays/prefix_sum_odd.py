def prefix_sum_odd (A,B):
    p_sum_odd = [i for i in range(len(A))]
    p_sum_odd[0] = 0
    result = []
    for i in range(1,len(A)):
        if(i%2==1):
            p_sum_odd[i] = p_sum_odd[i-1] + A[i]
        else:
            p_sum_odd[i] = p_sum_odd[i-1]
    for i in range(len(B)):
        index1 = B[i][0]
        index2 = B[i][1]
        if(index1 == 0 or index2==0):
            result.append(p_sum_odd[index2])
        else:
            result.append(p_sum_odd[index2]-p_sum_odd[index1-1])
    return result        



A = [2, 8, 3, 9, 15]
B = [ [1, 4], 
      [0, 2], 
      [2, 3] ]
print(prefix_sum_odd(A,B))