import sys
input=sys.stdin.readline
from collections import deque


N,M=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(M)]
v=[[0]*N for _ in range(M)]

def W_bfs(i,j):
    q=deque()
    q.append((i,j))
    v[i][j]=1
    W_cnt = 1

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<M and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]=='W'):
                q.append((ni,nj))
                v[ni][nj]=1
                W_cnt+=1

    return W_cnt**2

def B_bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    B_cnt=1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if (0 <= ni < M and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] == 'B'):
                q.append((ni, nj))
                v[ni][nj] = 1
                B_cnt+=1
    return B_cnt**2

W_answer=[]
B_answer=[]

for i in range(M):
    for j in range(N):
        if(v[i][j]==0 and arr[i][j]=='W'):
            W_answer.append(W_bfs(i,j))

        if(v[i][j]==0 and arr[i][j]=='B'):
            B_answer.append(B_bfs(i,j))

print(sum(W_answer), sum(B_answer))
