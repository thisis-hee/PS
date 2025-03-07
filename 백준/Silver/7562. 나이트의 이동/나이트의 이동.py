import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

T=int(input())

def bfs(si,sj, ei, ej):

    q=[]
    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj=q.pop(0)

        if((ci,cj)==(ei,ej)):
            return v[ci][cj]-1

        for di,dj in ((-2,-1),(2,-1),(2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<l and 0<=nj<l and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1

for _ in range(T):
    l=int(input())
    si,sj=map(int,input().split())
    ei,ej=map(int,input().split())
    arr=[[0]*l for _ in range(l)]
    v=[[0]*l for _ in range(l)]
    print(bfs(si,sj,ei,ej))
