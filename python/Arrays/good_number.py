def solve(ArrayGood,SumCount):
    i=0
    while(i<len(ArrayGood)-1):
        j=i+1
        while(j<=len(ArrayGood)-1):
            if(ArrayGood[i]+ArrayGood[j]==SumCount):
                print(ArrayGood[i]+ArrayGood[j])
                return 1
            j+=1
        i+=1    
    return 0  

# A = [1,2,3,4]
# B = 7            

# A = [1,2,2]
# B = 4
# A= [510827,351151,96897,925335,299818,192489,456948,44720,510589,598577]
# B = 808099
A=[1,2,3,4]
B= 7
solve(A,B)