N=int(input())

decimals = list(map(int,input().split()))

total=0
for i in range(N):
    count=0
    for j in range(2,decimals[i]+1):
        if(decimals[i]%j==0):
            count+=1
    if(count==1):
        total+=1

print(total)