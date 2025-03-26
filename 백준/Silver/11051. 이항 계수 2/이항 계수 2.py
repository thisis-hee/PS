import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
import math

N,K=map(int,input().split())

boonmo=1
for i in range(N,N-K,-1):
    boonmo*=i

boonja=1
for j in range(2,K+1):
    boonja*=j

print((boonmo//boonja)%10007)
