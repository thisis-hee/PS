import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
import math

N,M,K=map(int,input().split())

arr=[[0]*M for _ in range(N)]

for _ in range(K):
    a,b=map(int,input().split())
    arr[a-1][b-1]=1

v=[[0]*M for _ in range(N)]
cnt_list=[]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    v[i][j]=1
    cnt=1

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    cnt_list.append(cnt)


for i in range(N):
    for j in range(M):
        if(arr[i][j]==1 and v[i][j]==0):
            bfs(i,j)

print(max(cnt_list))