import sys

input=sys.stdin.readline

n=int(input())
answer=[]

for _ in range(n):
    a = list(input().split())
    answer.append(a)

answer.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in answer:
    print(i[0])