import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
v=[[-1]*m for _ in range(n)]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    v[i][j]=0

    while q:
        ci,cj=q.popleft()

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<n and 0<=nj<m and v[ni][nj]==-1):
                if(arr[ni][nj]==0):
                    v[ni][nj]=0
                elif(arr[ni][nj]==1):
                    v[ni][nj]=v[ci][cj]+1
                    q.append((ni,nj))


for i in range(n):
    for j in range(m):
        if(arr[i][j]==2 and v[i][j]==-1):
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(v[i][j], end=' ')
    print()
