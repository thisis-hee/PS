import sys
from collections import deque

# N -> K로 이동
# 뒤로 한 칸, 앞으로 한 칸, 앞으로 2배 이동 가능
# 동생은 0~100000에 위치해있음

input = sys.stdin.readline
N, K = map(int, input().split())
v = [0] * 100001


def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()

        if c == K:
            return v[c] - 1

        for n in (c - 1, c + 1, 2 * c):
            if 0 <= n <= 100000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1


print(bfs(N))
