import sys
from collections import deque
input = sys.stdin.readline

N,K,M=map(int,input().split())

ans=[]

people=deque([i for i in range(1,N+1)])

while people:
  for _ in range(M):
    for _ in range(K-1):
      people.append(people.popleft())
    ans.append(people.popleft())
    if(len(people)==0):
      break
  people=deque(list(people)[::-1])

for ans in ans:
  print(ans)