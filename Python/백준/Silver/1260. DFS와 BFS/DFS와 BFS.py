import sys
from collections import deque

input=sys.stdin.readline

def dfs(c):
    ans_dfs.append(c)
    v_dfs[c]=True

    for n in adj[c]:
        if(v_dfs[n]==False):
            dfs(n)

def bfs(s):
    q=[]
    q.append(s)

    ans_bfs.append(s)
    v_bfs[s]=True

    while(q!=[]):
        c=q.pop(0)
        for n in adj[c]:
            if(v_bfs[n]==False):
                q.append(n)
                ans_bfs.append(n)
                v_bfs[n]=True


N,M,V=map(int,input().split())

adj=[[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(len(adj)):
    adj[i].sort()

v_dfs=[False]*(N+1)
ans_dfs=[]
dfs(V)

v_bfs=[False]*(N+1)
ans_bfs=[]
bfs(V)

print(*ans_dfs)
print(*ans_bfs)