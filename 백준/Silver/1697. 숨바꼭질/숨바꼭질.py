import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

N,K=map(int,input().split())

def bfs(s,e):
    q=[]
    q.append(s)
    v=[0]*100001
    v[s]=1

    while q:
        c=q.pop(0)
        if(c==e):
            return v[c]-1

        for n in (c-1,c+1,2*c):
            if(0<=n<=100000 and v[n]==0):
                q.append(n)
                v[n]=v[c]+1

print(bfs(N,K))