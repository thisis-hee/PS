from collections import deque

def bfs(x,y,n):
    q=deque()
    q.append(x)
    v=[0]*1000001
    v[x]=1
    
    while q:
        c=q.popleft()
        
        if c == y:
            return v[c]
        
        for nnext in (c+n, c*2, c*3):
            if nnext <= 1000000 and v[nnext]==0:
                q.append(nnext)
                v[nnext]=v[c]+1
    
    return -1

def solution(x, y, n):
    
    answer = bfs(x,y,n)
    
    if answer == -1 :
        return -1
    else:
        return answer-1
        
    