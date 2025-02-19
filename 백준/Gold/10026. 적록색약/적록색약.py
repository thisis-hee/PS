import sys
input=sys.stdin.readline

def bfs(si,sj):
    q=[]
    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj=q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<N and arr[ni][nj]==arr[ci][cj] and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj]=1

N=int(input())
arr=[list(input().rstrip()) for _ in range(N)]

# 여기까지는 완성함. 아래부턴 참고해서 풂
# visited를 적록색약인 경우, 아닌 경우 나누어서 해야됨.
# 적록색약이 아닌 경우
v = [[0] * N for _ in range(N)]
cnt1=0
for i in range(N):
    for j in range(N):
        if(v[i][j]==0):
            bfs(i,j)
            cnt1+=1

# 적록색약인 경우
v = [[0] * N for _ in range(N)]
cnt2=0

for i in range(N):
    for j in range(N):
        if(arr[i][j]=='R'):
            arr[i][j]='G'

for i in range(N):
    for j in range(N):
        if(v[i][j]==0):
            bfs(i,j)
            cnt2+=1

print(cnt1, cnt2)