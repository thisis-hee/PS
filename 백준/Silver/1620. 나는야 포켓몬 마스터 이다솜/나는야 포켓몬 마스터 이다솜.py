import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

N,M=map(int,input().split())

num_dict={}
poke_dict={}

for i in range(1, N+1):
    pokemon_name=input().rstrip()
    poke_dict[pokemon_name]=i
    num_dict[i]=pokemon_name

for j in range(M):
    check=input().rstrip()
    if(check.isalpha()):
        print(poke_dict[check])
    else:
        print(num_dict[int(check)])