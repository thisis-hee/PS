import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

N,K=map(int,input().split())
temp_list=list(map(int,input().split()))
v=[0]*(N-K+1)
v[0]=sum(temp_list[0:K])
for i in range(1,N-K+1):
    v[i]=v[i-1]-temp_list[i-1]+temp_list[i+K-1]

print(max(v))