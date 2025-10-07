import sys
from itertools import permutations

input = sys.stdin.readline

num = input().rstrip()

if '0' not in num:
    print(-1)
else:
    total = sum(map(int, num))
    if total % 3 != 0:
        print(-1)
    else:
        print(''.join(sorted(num, reverse=True)))