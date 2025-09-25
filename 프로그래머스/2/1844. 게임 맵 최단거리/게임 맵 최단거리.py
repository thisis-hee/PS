from collections import deque

def bfs(si,sj,maps):
    n,m=len(maps),len(maps[0])
    q=deque()
    q.append((si,sj))
    v=[[0]*m for _ in range(n)]
    v[si][sj]=1
    
    while q:
        ci,cj=q.popleft()
        
        if((ci,cj)==(n-1,m-1)):
            return v[ci][cj]
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if(0<=ni<n and 0<=nj<m and maps[ni][nj]==1 and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return -1


def solution(maps):
    answer=bfs(0,0,maps)
    return answer