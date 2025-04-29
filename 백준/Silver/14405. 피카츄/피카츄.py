import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

s=input().rstrip()

s=s.replace('pi', ' ')
s=s.replace('ka', ' ')
s=s.replace('chu', ' ')

if(len(s.strip())==0):
    print("YES")
else:
    print("NO")



