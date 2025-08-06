import sys
from collections import deque

A, K = map(int, input().split())
v = [0] * (K + 1)


def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 0

    while q:
        c = q.popleft()
        if c == K:
            break

        for n in (2 * c, c + 1):
            if n <= K and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1


bfs(A)
print(v[K])
