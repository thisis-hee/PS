import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

F,S,G,U,D=map(int,input().split())

def bfs(s, e):
    q=[]
    q.append(s)
    v=[0]*(F+1)
    v[s]=1

    while q:
        c=q.pop(0)
        if(c==e):
            return v[c]-1

        for n in (c+U,c-D):
            if(1<=n<=F and v[n]==0):
                q.append(n)
                v[n]=v[c]+1
    return "use the stairs"

print(bfs(S,G))
