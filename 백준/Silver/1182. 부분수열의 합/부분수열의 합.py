import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations

N,S=map(int,input().split())
num_list=list(map(int,input().split()))

cnt=0

for i in range(1,N+1):
    for j in combinations(num_list,i):
        if(sum(j)==S):
            cnt+=1

print(cnt)