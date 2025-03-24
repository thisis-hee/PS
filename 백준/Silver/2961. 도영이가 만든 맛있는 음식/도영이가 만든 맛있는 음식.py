import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

N=int(input())
flavor_list=[]
total_list=[]

for _ in range(N):
    flavor_list.append(list(map(int,input().split())))

for i in range(1, len(flavor_list)+1):
    for j in combinations(flavor_list,i):
        S=1
        B=0
        for k in range(len(j)):
            S*=j[k][0]
            B+=j[k][1]

        total_list.append(abs(S-B))

print(min(total_list))
