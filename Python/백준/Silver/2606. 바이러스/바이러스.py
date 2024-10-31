import sys
from collections import deque

input=sys.stdin.readline

def dfs(c):
    ans.append(c)
    v[c]=True

    for i in adj[c]:
        if(v[i]==False):
            dfs(i)


N=int(input())
E=int(input())

adj=[[] for _ in range(N+1)]

for _ in range(E):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

ans=[]
v=[False]*(N+1)
dfs(1)

print(len(ans)-1)