import sys
import heapq

N = int(input())
s = []


for _ in range(N):
    num = int(sys.stdin.readline())*-1
    if num != 0:
        heapq.heappush(s, num)
    else:
        if(len(s)!=0):
            print(-1*heapq.heappop(s))
        else:
            print(0)