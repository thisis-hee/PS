import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]
ans = []

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    adj[a].append(b)
    adj[b].append(a)

for i in range(len(adj)):
    adj[i].sort()


def bfs(s):
    q = deque()
    q.append(s)
    v = [0 for _ in range(N + 1)]
    v[s] = 1

    while q:
        c = q.popleft()

        for n in adj[c]:
            if (v[n] == 0):
                q.append(n)
                v[n] = v[c] + 1

    return max(v) - 1


for i in range(1, N + 1):
    ans.append(bfs(i))

print(min(ans), ans.count(min(ans)))
result = []
for i in range(len(ans)):
    if ans[i] == min(ans):
        result.append(i + 1)

print(*result)
