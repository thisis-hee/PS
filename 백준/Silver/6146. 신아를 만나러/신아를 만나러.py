import sys
from collections import deque

input = sys.stdin.readline

X, Y, N = map(int, input().split())
X += 500
Y += 500
water = []

for _ in range(N):
    x, y = map(int, input().split())
    water.append((x + 500, y + 500))

arr = [[0] * 1001 for _ in range(1001)]
v = [[0] * 1001 for _ in range(1001)]

for i, j in water:
    arr[i][j] = 1


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (X, Y):
            return v[ci][cj]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if (0 <= ni < 1000 and 0 <= nj < 1000 and v[ni][nj] == 0 and arr[ni][nj] != 1):
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))


print(bfs(500, 500) - 1)