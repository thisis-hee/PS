import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    M,N,K=map(int,input().split())

    arr=[[0]*M for _ in range(N)]

    for _ in range(K):
        a,b=map(int,input().split())
        arr[b][a]=1

    v=[[0]*M for _ in range(N)]

    cnt=0

    def bfs(si,sj):
        q=[]
        q.append((si,sj))
        v[si][sj]=1

        while q:
            ci,cj=q.pop(0)

            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=ci+di,cj+dj
                if(0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0):
                    q.append((ni,nj))
                    v[ni][nj]=1
        return

    for i in range(N):
        for j in range(M):
            if(arr[i][j]==1 and v[i][j]==0):
                bfs(i,j)
                cnt+=1

    print(cnt)