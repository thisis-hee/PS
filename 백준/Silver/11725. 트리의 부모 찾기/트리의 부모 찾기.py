import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

N=int(input())
adj=[[] for _ in range(N+1)]
ans=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

v=[0]*(N+1)

def dfs(c):
    v[c]=1

    for n in adj[c]:
        if(v[n]==0):
            ans[n].append(c)
            v[n]=1
            dfs(n)

dfs(1)

for i in range(2,N+1):
    print(*ans[i])