import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations

# 0 빈칸, 1 벽, 2 바이러스
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

safety_list=[]
wall_list=[]

def bfs(i,j):
    q=deque()
    q.append((i,j))

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<M and new_arr[ni][nj]==0):
                q.append((ni,nj))
                new_arr[ni][nj]=2


# 벽을 세울 수 있는 좌표 = 0의 좌표
for i in range(N):
    for j in range(M):
        if(arr[i][j]==0):
            wall_list.append((i,j))

# 벽 3개 세우는 경우의 수
for wall in combinations(wall_list,3):
    new_arr=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_arr[i][j]=arr[i][j]
    new_arr[wall[0][0]][wall[0][1]]=1
    new_arr[wall[1][0]][wall[1][1]]=1
    new_arr[wall[2][0]][wall[2][1]]=1

    for i in range(N):
        for j in range(M):
            if(new_arr[i][j]==2):
                bfs(i,j)

    cnt=0

    for i in range(N):
        for j in range(M):
            if(new_arr[i][j]==0):
                cnt+=1

    safety_list.append(cnt)

print(max(safety_list))