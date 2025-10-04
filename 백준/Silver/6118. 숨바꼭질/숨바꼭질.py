import sys
sys.setrecursionlimit(1000000)
from collections import deque

input = sys.stdin.readline

a,b=map(int,input().split())

def bfs(s):
    q=deque()
    q.append(s)
    v[s]=1

    while q:
        c=q.popleft()
        for n in arr[c]:
            if v[n]==0:
                q.append(n)
                v[n]+=v[c]+1

arr=[[] for _ in range(a+1)]
v=[0]*(a+1)

for _ in range(b):
    c,d=map(int,input().split())
    arr[c].append(d)
    arr[d].append(c)

for i in range(1, len(arr)):
    arr[i].sort()

bfs(1)

print(v.index(max(v)), v[v.index(max(v))]-1, v.count(max(v)))