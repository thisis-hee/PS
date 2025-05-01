import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    for _ in range(M):
        a,b=map(int,input().split())

    print(N-1)