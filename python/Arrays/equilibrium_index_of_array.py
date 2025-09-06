class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix_sum = [0 for i in range(len(A))]
        prefix_sum[0] = A[0]
        for i in range(1,len(A)):
            prefix_sum[i] = prefix_sum[i-1] + A[i]
        for i in range(len(A)):
            if(i==0):
                if((prefix_sum[len(A)-1]-prefix_sum[0])==0):
                    return i
            if(i==len(A)-1):
                if(prefix_sum[i-1]==0):
                    return i
            if(prefix_sum[i-1]==(prefix_sum[len(A)-1] - prefix_sum[i])):
                return i    
        return -1        

        

