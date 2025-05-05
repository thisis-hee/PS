import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
import math

N=int(input())

name_list=[]

for _ in range(N):
    name_list.append(input().rstrip())

name_list_asc=sorted(name_list)
name_list_desc=sorted(name_list, reverse=True)

if(name_list==name_list_desc):
    print("DECREASING")
elif(name_list==name_list_asc):
    print("INCREASING")
else:
    print("NEITHER")