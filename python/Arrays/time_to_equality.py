def functionMax(A):
    sumt=0
    maximum = max(A)
    for i in A:
        sumt =sumt+ maximum - i
    print(sumt)    