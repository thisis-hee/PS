import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

N, K = map(int,input().split())
coin_list=[]
for _ in range(N):
    coin_list.append(int(input()))

total=0
cnt=0
next_num=deepcopy(K)

while(total!=K):
    for i in range(len(coin_list)-1,-1,-1):
        if(coin_list[i]>next_num):
            continue
        else:
            cnt+=next_num//coin_list[i]
            total += coin_list[i] * (next_num // coin_list[i])
            next_num=next_num-(coin_list[i]*(next_num//coin_list[i]))

            break

print(cnt)