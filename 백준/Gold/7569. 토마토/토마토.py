import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

M,N,H=map(int,input().split())
arr=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

start=deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if(arr[i][j][k]==1):
                start.append((i,j,k))



def bfs():
    while start:
        ci,cj,ck=start.popleft()
        for di,dj,dk in ((0,-1,0),(0,1,0),(0,0,1),(0,0,-1),(-1,0,0),(1,0,0)):
            ni,nj,nk=ci+di,cj+dj,ck+dk
            if(0<=ni<H and 0<=nj<N and 0<=nk<M and arr[ni][nj][nk]==0):
                start.append((ni,nj,nk))
                arr[ni][nj][nk]=arr[ci][cj][ck]+1

bfs()
res=0

for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            res=max(res,k)
print(res - 1)