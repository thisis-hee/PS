import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

people = deque([i for i in range(1, n + 1)])
result = []

while people:
    for _ in range(k - 1):
        people.append(people.popleft())

    result.append(people.popleft())

print('<', end='')
for i in range(len(result) - 1):
    print(result[i], end='')
    print(', ', end='')
print(result[-1], end='')
print('>')