A=list(map(int,input().split(' ')))
A.sort()

if(A[0]+A[1]>A[2]):
    print(sum(A))
else:
    print(2*(A[0]+A[1])-1)