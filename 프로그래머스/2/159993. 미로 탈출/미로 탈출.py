from collections import deque

def bfs_Lever(si, sj, maps, v1):
    q=deque()
    q.append((si,sj))
    v1[si][sj]=1
    
    while q:
        ci, cj = q.popleft()
        
        if maps[ci][cj]=='L':
            return v1[ci][cj]
        
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<len(maps) and 0<=nj<len(maps[0]) and maps[ni][nj]!='X' and v1[ni][nj]==0:
                q.append((ni,nj))
                v1[ni][nj]=v1[ci][cj]+1
    
    return -1

def Lever_to_End(si, sj, maps, v2):
    q=deque()
    q.append((si,sj))
    v2[si][sj]=0
    
    while q:
        ci, cj = q.popleft()
        
        if maps[ci][cj]=='E':
            return v2[ci][cj]
        
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<len(maps) and 0<=nj<len(maps[0]) and maps[ni][nj]!='X' and v2[ni][nj]==0:
                q.append((ni,nj))
                v2[ni][nj]=v2[ci][cj]+1
    
    return -1


def solution(maps):
    answer = 0
    
    maps = [list(i) for i in maps]
    v1=[[0]*len(maps[0]) for _ in range(len(maps))]
    v2=[[0]*len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                answer1 = bfs_Lever(i, j, maps, v1)
    
    if answer1 == -1:
        return -1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                answer2 = Lever_to_End(i, j, maps, v2)
    
    if answer2 == -1:
        return -1
    
    return answer1+answer2-1

