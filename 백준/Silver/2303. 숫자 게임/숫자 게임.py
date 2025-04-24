import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

N=int(input())
card_list=[]
for _ in range(N):
    card_list.append(list(map(int,input().split())))

num_list=[]
maxx=0
cnt=1
for i in range(N):
    min=0
    for j in combinations(card_list[i],3):
        min=max(min,sum(j)%10)
    if(maxx<=min):
        maxx=min
        cnt=i+1


print(cnt)