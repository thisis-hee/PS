# heapq 알면 쉬움
import sys
import heapq

N = int(input())
s = []


for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(s, num)
    else:
        if(len(s)!=0):
            print(heapq.heappop(s))
        else:
            print(0)
