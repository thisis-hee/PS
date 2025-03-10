import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

M,N=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

start=deque()

for i in range(N):
    for j in range(M):
        if(arr[i][j]==1):
            start.append((i,j))



def bfs():
    while start:
        ci,cj=start.popleft()
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<M and arr[ni][nj]==0):
                start.append((ni,nj))
                arr[ni][nj]=arr[ci][cj]+1

bfs()
res=0

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)