import sys
input=sys.stdin.readline

def bfs(si,sj):
    q=[]
    q.append((si,sj))
    v[si][sj]=1
    size=1

    while q:
        ci,cj=q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<M and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=1):
                q.append((ni,nj))
                v[ni][nj]=1
                size+=1
    return size

M,N,K=map(int,input().split())
arr=[[0]*N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[j][i]=1

v=[[0]*N for _ in range(M)]
cnt_list=[]

for i in range(M):
    for j in range(N):
        if(arr[i][j]==0 and v[i][j]==0):
            cnt_list.append(bfs(i,j))

print(len(cnt_list))
print(*sorted(cnt_list))