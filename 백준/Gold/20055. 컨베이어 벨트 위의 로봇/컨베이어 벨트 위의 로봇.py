import sys
input=sys.stdin.readline
from collections import deque

N,K=map(int,input().split())
belt=deque(map(int,input().split()))
robot=deque([0]*N)
cnt=0

while True:
    cnt+=1
    belt.rotate(1)
    robot[-1]=0
    robot.rotate(1)
    robot[-1]=0

    for j in range(len(robot)-2,-1,-1):
        if(robot[j]==1 and robot[j+1]==0 and belt[j+1]>=1):
            robot[j+1]=1
            robot[j]=0
            belt[j+1]-=1
    
    if (robot[0] == 0 and belt[0] >= 1):
        robot[0] = 1
        belt[0] -= 1

    if(belt.count(0)>=K):
        break

print(cnt)
