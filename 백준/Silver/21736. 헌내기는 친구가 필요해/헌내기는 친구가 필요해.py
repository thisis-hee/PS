import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(input().rstrip()))

v = [[0] * M for _ in range(N)]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 0

    while q:
        ci, cj = q.popleft()

        if arr[ci][cj] == 'P':
            cnt += 1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'X' and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
    return cnt

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            answer=bfs(i,j)

if answer == 0:
    print('TT')
else:
    print(answer)
