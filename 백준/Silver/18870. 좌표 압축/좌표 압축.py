import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

N=int(input())
X=list(map(int,input().split()))


X_sort = sorted(list(set(X)))

dic = {}
for i in range(len(X_sort)):
  dic[X_sort[i]] = i

for i in X:
  print(dic[i], end=" ")