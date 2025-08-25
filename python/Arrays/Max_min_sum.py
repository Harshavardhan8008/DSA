def MaxMinSum(ArraySum):
   minimum=ArraySum[0]
   maximum=ArraySum[0]
   for i in range(1,len(ArraySum)):
       if(ArraySum[i]>maximum):
           maximum= ArraySum[i]
       if(ArraySum[i]<minimum):
           minimum= ArraySum[i]
   print(minimum+maximum)        
   return minimum + maximum


A = [-2, 1, -4, 5, 3]
MaxMinSum(A)
