import sys
input=sys.stdin.readline
from collections import deque

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
v=[[0]*M for _ in range(N)]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    v[i][j]=1

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=1

cnt=0
for i in range(N):
    for j in range(M):
        if(arr[i][j]==1 and v[i][j]==0):
            bfs(i,j)
            cnt+=1

print(cnt)