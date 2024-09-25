from itertools import combinations
import math

T=int(input())


for _ in range(T):
    gcd_total=0
    num_list=list(map(int,input().split()))
    real_list=num_list[1:]
    for i in range(len(list(combinations(real_list,2)))):
        gcd_total+=math.gcd(list(combinations(real_list,2))[i][0],list(combinations(real_list,2))[i][1])
    print(gcd_total)