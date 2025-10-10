import sys
from itertools import permutations

input = sys.stdin.readline

n=int(input())
k=int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

answer = set()

for i in permutations(num_list, k):
    strr = ''
    for j in i:
        strr = strr+str(j)
    answer.add(int(strr))

print(len(answer))