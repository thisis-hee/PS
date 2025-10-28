import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < a and 0 <= nj < b and arr[ni][nj] == '#' and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1


for _ in range(T):
    a, b = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(a)]
    v = [[0] * b for _ in range(a)]

    cnt = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '#' and v[i][j] == 0:
                cnt += 1
                bfs(i, j)
    print(cnt)
