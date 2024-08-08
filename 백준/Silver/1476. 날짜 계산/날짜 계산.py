ESM=list(map(int,input().split()))
A=[1,1,1]
year=1
while(True):
    if(A==ESM):
        break
    
    A[0]+=1
    A[1]+=1
    A[2]+=1
    if(A[0]>15):
        A[0]=1
    if(A[1]>28):
        A[1]=1
    if(A[2]>19):
        A[2]=1
    year+=1

print(year)