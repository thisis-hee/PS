N=int(input())

student=[i for i in range(N)]

order=list(map(int,input().split()))

ans=[]

for i in range(N):
    if(order[i]==0):
        ans.append(student[i]+1)
    else:
        ans.insert(len(ans)-order[i],student[i]+1)

print(*ans)