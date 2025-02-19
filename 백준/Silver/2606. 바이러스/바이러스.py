import sys
input=sys.stdin.readline

def dfs(c):
    v[c]=1
    for n in adj[c]:
        if(v[n]==0):
            dfs(n)

N=int(input())
M=int(input())

adj=[[] for _ in range(N+1)]
v=[0]*(N+1)

for _ in range(M):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

dfs(1)
print(sum(v)-1)