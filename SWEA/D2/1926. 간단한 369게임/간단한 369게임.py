N=int(input())

for i in range(1,N+1):
    A=list(str(i))
    count=0
    for j in range(len(A)):
        if(A[j]=='3' or A[j]=='6' or A[j]=='9'):
            count+=1
           
    
    if(count==0):
        print(''.join(A), end=' ')
    else:
        print(count*'-', end=' ')
            
