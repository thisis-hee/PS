import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
import math

N=int(input())
M=int(input())
adj=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

friend=set()

for n in adj[1]:
    friend.add(n)
    for i in adj[n]:
        friend.add(i)

if(len(friend)==0):
    print(0)
else:
    print(len(friend)-1)