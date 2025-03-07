import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

v=[[0]*m for _ in range(n)]

width=[]

def bfs(si,sj):
    q=[]
    q.append((si,sj))
    v[si][sj]=1
    cnt=1

    while q:
        ci,cj=q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt

for i in range(n):
    for j in range(m):
        if(arr[i][j]==1 and v[i][j]==0):
            width.append(bfs(i,j))

if(width==[]):
    print(0)
    print(0)
else:
    print(len(width))
    print(max(width))
