import sys
input = sys.stdin.readline

import math
from itertools import combinations

T=int(input())

for _ in range(T):
    num_list=list(map(int,input().split()))
    max_gcd=1
    for i,j in combinations(num_list,2):
        max_gcd=max(max_gcd, math.gcd(i,j))
    print(max_gcd)