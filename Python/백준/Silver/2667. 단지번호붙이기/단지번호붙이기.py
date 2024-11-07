#import sys
#input=sys.stdin.readline

def bfs(si,sj):
    q=[]
    q.append((si,sj))
    v[si][sj]=1
    count=1

    while q:
        ci,cj=q.pop(0)
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<N and v[ni][nj]==0 and map[ni][nj]==1):
                q.append((ni,nj))
                v[ni][nj]=1
                count+=1

    return count



N=int(input())
map=[list(map(int, input())) for _ in range(N)]
v=[[0]*(N) for _ in range(N)]
ans=[]

for i in range(N):
    for j in range(N):
        if(map[i][j]==1 and v[i][j]==0):
            ans.append(bfs(i,j))

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])