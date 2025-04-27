import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

def bfs(si,sj,v):
    q=deque()
    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(v[ni][nj]==0 and arr[ni][nj]>0):
                q.append((ni,nj))
                v[ni][nj]=1

def solve():
    for year in range(1,900000):
        a_sub=[[0]*M for _ in range(N)]
        for i in range(1,N-1):
            for j in range(1,M-1):
                sub=0
                if(arr[i][j]>0):
                    if(arr[i-1][j]==0):
                        sub+=1
                    if(arr[i+1][j]==0):
                        sub+=1
                    if(arr[i][j-1]==0):
                        sub+=1
                    if(arr[i][j+1]==0):
                        sub+=1
                a_sub[i][j]+=sub

        for i in range(1,N-1):
            for j in range(1,M-1):
                if(a_sub[i][j]>0):
                    arr[i][j]=max(0,arr[i][j]-a_sub[i][j])

        v=[[0]*M for _ in range(N)]
        cnt=0
        for i in range(1,N-1):
            for j in range(1,M-1):
                if(v[i][j]==0 and arr[i][j]>0):
                    bfs(i,j,v)
                    cnt+=1
                    if(cnt>1):
                        return year
        if(cnt==0):
            return 0

ans=solve()
print(ans)