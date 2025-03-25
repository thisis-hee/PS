import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations

N=int(input())
num_list=list(map(int,input().split()))
sum_list=[]

for i in permutations(num_list, len(num_list)):
    sum=0
    for j in range(len(num_list)-1):
        sum+=abs(i[j]-i[j+1])
    sum_list.append(sum)

print(max(sum_list))