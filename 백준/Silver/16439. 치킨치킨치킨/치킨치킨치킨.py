import sys
input=sys.stdin.readline
from itertools import combinations

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
arr_list=[x for x in range(M)]
total=0

for i in combinations(arr_list,3):
    tot=0
    for j in range(len(arr)):
        tot+=max(arr[j][i[0]],arr[j][i[1]],arr[j][i[2]])
    total=max(total,tot)

print(total)