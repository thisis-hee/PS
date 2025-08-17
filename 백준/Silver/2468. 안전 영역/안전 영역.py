import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_num=0

for i in arr:
    for j in i:
        if j > max_num :
            max_num = j

def bfs(si,sj,rain_height):
    q=deque()
    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj=q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<N and arr[ni][nj]>rain_height and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=1

answer=[]

for i in range(max_num):
    cnt=0
    v=[[0]*N for _ in range(N)]

    for j in range(N):
        for k in range(N):
            if(arr[j][k]>i and v[j][k]==0):
                bfs(j,k,i)
                cnt+=1
    answer.append(cnt)

print(max(answer))