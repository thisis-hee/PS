import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

def dfs(ci,cj):
    v[ci][cj]=1

    if(arr[ci][cj]==1):
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<h and 0<=nj<w and arr[ni][nj]==1 and v[ni][nj]==0):
                dfs(ni,nj)

while True:

    w,h=map(int,input().split())
    if(w==0 and h==0):
        break

    arr=[]

    for _ in range(h):
        a=list(map(int,input().split()))
        arr.append(a)

    v=[[0]*w for _ in range(h)]

    cnt=0

    for i in range(h):
        for j in range(w):
            if(arr[i][j]==1 and v[i][j]==0):
                dfs(i,j)
                cnt+=1

    print(cnt)
