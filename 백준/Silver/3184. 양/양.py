import sys
from collections import deque

R,C=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(R)]
v=[[0]*C for _ in range(R)]
total_wolf=0
total_sheep=0

def bfs(si,sj):
    global total_wolf
    global total_sheep
    q=deque()
    q.append((si,sj))
    v[si][sj]=1
    wolf_cnt=0
    sheep_cnt=0
    if(arr[si][sj]=='v'):
        wolf_cnt+=1
    elif(arr[si][sj]=='o'):
        sheep_cnt+=1

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<R and 0<=nj<C and arr[ni][nj]!='#' and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=1
                if(arr[ni][nj]=='v'):
                    wolf_cnt+=1
                elif(arr[ni][nj]=='o'):
                    sheep_cnt+=1

    if(wolf_cnt>=sheep_cnt):
        total_wolf+=wolf_cnt
    else:
        total_sheep+=sheep_cnt

for i in range(R):
    for j in range(C):
        if(arr[i][j]!='#' and v[i][j]==0):
            bfs(i,j)

print(total_sheep, total_wolf)