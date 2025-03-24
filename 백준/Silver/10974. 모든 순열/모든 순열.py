import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

N=int(input())

num=[x for x in range(1,N+1)]

for i in permutations(num):
    print(*i)
