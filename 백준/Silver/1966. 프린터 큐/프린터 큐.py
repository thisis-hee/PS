import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    imp=deque(list(map(int,input().split())))
    idx=deque([x for x in range(N)])
    cnt=0
    while True:
        if(imp[0]>=max(imp)):
            imp.popleft()
            cnt+=1
            if(idx.popleft()==M):
                print(cnt)
                break
        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())