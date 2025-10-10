import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dance = set()

for _ in range(N):
    a, b = input().split()

    if 'ChongChong' in a or 'ChongChong' in b:
        dance.add(a)
        dance.add(b)

    if a in dance:
        dance.add(b)

    if b in dance:
        dance.add(a)

print(len(dance))