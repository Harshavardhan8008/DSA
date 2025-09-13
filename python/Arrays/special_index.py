def solve(A):
    count=0
    prefix_sum_even = [0 for i in range(len(A))]
    prefix_sum_odd = [0 for i in range(len(A))]
    prefix_sum_even[0] = A[0]
    prefix_sum_odd[0] = 0
    for i in range(1,len(A)):
        if(i%2==0):
            prefix_sum_even[i] = prefix_sum_even[i-1] + A[i]
            prefix_sum_odd[i] = prefix_sum_odd[i-1]
        else:
            prefix_sum_odd[i] = prefix_sum_odd[i-1] + A[i]        
            prefix_sum_even[i] = prefix_sum_even[i-1]
    def calculate_sum_range(Array,index1,index2):
        if(index2<0):
            return 0
        if(index1==0):
            return Array[index2]
        return Array[index2] - Array[index1-1]
    for i in range(len(A)):
        sum_prev = 0
        sum_next= 0
        #calculate previous sum of i
        #i.e. sumeven + sumodd from 0 to i-1
        sum_prev = calculate_sum_range(prefix_sum_even,0,i-1) +  calculate_sum_range(prefix_sum_odd,0,i-1)
        sum_next = calculate_sum_range(prefix_sum_even,i+1,len(A)-1) + calculate_sum_range(prefix_sum_odd,i+1,len(A)-1)
        if(sum_next==sum_prev):
            count+=1
    print(count,'count')        
    return count   
    
A=[1,2,3,7,1,2,3]    

solve(A)