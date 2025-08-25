def reverse_array(Array,A,B):
    # for i in range(A,int((B+A)/2)):
    #     print('coming',Array[i],Array[A+B-i])
    #     temp = Array[i]
    #     Array[i] =  Array[A+B-i]
    #     Array[A+B-i] = temp
    i=A
    j=B
    while(i<j):
        temp = Array[i]
        Array[i] =  Array[j]
        Array[j] = temp
        i+=   1
        j-=1

    print(Array)    

# A=[3,5,6,8,1]    

# A = [1, 2, 3, 4]
# B = 2
# C = 3

A = [2, 5, 6]
B = 0
C = 2

reverse_array(A,B,C)

