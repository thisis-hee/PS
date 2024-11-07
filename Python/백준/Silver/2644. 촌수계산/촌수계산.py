import sys
input=sys.stdin.readline

N=int(input())
a,b=map(int,input().split())
M=int(input())

def bfs(start, end):
    q=[]
    q.append(start)
    v=[0]*(N+1)
    v[start]=1

    while q:
        c=q.pop(0)
        for n in adj[c]:
            if(v[n]==0):
                q.append(n)
                v[n]+=v[c]+1

    if(v[end]!=0):
        return v[end]-1
    else:
        return -1

adj=[[] for _ in range(N+1)]

for _ in range(M):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

ans=bfs(a,b)
print(ans)