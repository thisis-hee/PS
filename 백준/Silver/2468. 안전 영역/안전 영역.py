import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

N=int(input())

arr=[list(map(int,input().split())) for _ in range(N)]
ans=[]

def dfs(i,j):
    v[i][j]=1

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=di+i,dj+j
        if(0<=ni<N and 0<=nj<N and new_arr[ni][nj]>0 and v[ni][nj]==0):
            dfs(ni,nj)

for i in range(0,max(map(max,arr))):
    cnt=0
    new_arr=[[0]*N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            new_arr[x][y]=arr[x][y]-i

    v=[[0]*N for _ in range(N)]

    for m in range(N):
        for n in range(N):
            if(v[m][n]==0 and new_arr[m][n]>0):
                dfs(m,n)
                cnt+=1

    ans.append(cnt)

print(max(ans))