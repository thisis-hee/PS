A=list(map(int,input().split()))

asc_A=sorted(A)
dsc_A=sorted(A,reverse=True)

if(A==asc_A):
    print('ascending')
elif(A==dsc_A):
    print('descending')
else:
    print('mixed')