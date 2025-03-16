import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

N,M=map(int,input().split())

adj=[[] for _ in range(N+1)]
v=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(c):
    v[c]=1

    for n in adj[c]:
        if(v[n]==0):
            dfs(n)

cnt=0

for i in range(1,N+1):
    if(v[i]==0):
        dfs(i)
        cnt+=1

print(cnt)