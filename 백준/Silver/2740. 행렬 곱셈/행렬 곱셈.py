import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

N1,M1=map(int,input().split())
arr1=[list(map(int,input().split())) for _ in range(N1)]

N2,M2=map(int,input().split())
arr2=[list(map(int,input().split())) for _ in range(N2)]

answer=[[0]*M2 for _ in range(N1)]

for i in range(N1):
    for j in range(M2):
        for k in range(N2):
            answer[i][j]+=arr1[i][k]*arr2[k][j]

for val in answer:
    print(*val)