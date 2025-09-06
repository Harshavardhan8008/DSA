# def noble_integer(A):
#     count=0
#     uniqueCount = 0
#     B = sorted(A,reverse=True)
#     for i in range(1,len(A)):
#         if(B[i-1]!=B[i]):
#             uniqueCount+=1
#         if(B[i]==uniqueCount):
#             count+=1
#         print(B[i],uniqueCount,)    
#     if(count):
#         return count
#     else:
#         return -1   

# def solve(self, A):
#     B = sorted(A,reverse=True)
#     for i in range(len(B)):
#         if(B[i]==i):
#             return 1
#     else:
#         return 1    

def solve(self, A):
    B = sorted(A,reverse=True)
    count=0
    if(count==B[0]):
        return 1
    for i in range(1,len(B)):
        if(B[i]==B[i-1]):
            count+=1
            if(B[i]==i-count):
                return 1
        else:
            count = 0 
            if(i==B[i]):
                return 1       
    else:
        return -1  





A = [3, 2, 1, 3]

# A = [1, 1, 3, 3]

print(noble_integer(A))
