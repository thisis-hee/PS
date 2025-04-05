import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
chicken=[]
home=[]
chicken_distance=[]

for i in range(N):
    for j in range(N):
        if(arr[i][j]==2):
            chicken.append((i,j))
        if(arr[i][j]==1):
            home.append((i,j))

for i in combinations(chicken,M):
    min_chicken_distance=0
    for home_i,home_j in home:
        min_distance=100
        for chicken_i,chicken_j in i:
            min_distance=min(min_distance,abs(home_i-chicken_i)+abs(home_j-chicken_j))
        min_chicken_distance+=min_distance
    chicken_distance.append(min_chicken_distance)

print(min(chicken_distance))
