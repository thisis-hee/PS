import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

def dfs(ci,cj):
    global cnt
    v[ci][cj]=1
    if(arr[ci][cj]=='P'):
        cnt+=1

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=ci+di,cj+dj
        if(0<=ni<n and 0<=nj<m and arr[ni][nj]!='X' and v[ni][nj]==0):
            dfs(ni,nj)


n,m=map(int,input().split())

arr=list(list(input().rstrip()) for _ in range(n))
v=[[0]*m for _ in range(n)]
cnt=0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if(arr[i][j]=='I'):
            dfs(i,j)


if(cnt!=0):
    print(cnt)
else:
    print('TT')