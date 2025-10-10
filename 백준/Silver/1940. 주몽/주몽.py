import sys
from collections import deque

input = sys.stdin.readline

N=int(input())
M=int(input())

num_list=list(map(int,input().split()))
num_list.sort()

num_list=deque(num_list)

answer=0
left=0
right=N-1

while left<right:
    if num_list[left]+num_list[right]==M:
        answer+=1
        left+=1
        right-=1
    elif num_list[left]+num_list[right]>M:
        right-=1
    elif num_list[left]+num_list[right]<M:
        left+=1

print(answer)