import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

N=int(input())

daegeun=deque()
youngsik=deque()

for _ in range(N):
    daegeun.append(input().rstrip())

for _ in range(N):
    youngsik.append(input().rstrip())

cnt=0

while youngsik:
    if (daegeun[0] == youngsik[0]):
        daegeun.popleft()
        youngsik.popleft()
    else:
        daegeun.remove(youngsik.popleft())
        cnt+=1

print(cnt)