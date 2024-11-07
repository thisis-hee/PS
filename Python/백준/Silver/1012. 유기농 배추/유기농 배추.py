T = int(input())


def bfs(si, sj):
    q = []
    q.append((si, sj))
    v[si][sj] = 1
    count = 1

    while q:
        ci,cj=q.pop(0)
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj=ci+di,cj+dj
            if(0<=ni<N and 0<=nj<M and matrix[ni][nj]==1 and v[ni][nj]==0):
                q.append((ni,nj))
                v[ni][nj] = 1
                count+=1

    return count


for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    ans = []

    for _ in range(K):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    for i in range(N):
        for j in range(M):
            if (matrix[i][j] == 1 and v[i][j] == 0):
                ans.append(bfs(i, j))


    print(len(ans))