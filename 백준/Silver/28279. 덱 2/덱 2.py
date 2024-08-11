from collections import deque
import sys
N=int(sys.stdin.readline())
a=deque()

for _ in range(N):
    command=sys.stdin.readline().split()
    if(command[0]=='1'):
        a.appendleft(command[1])
    elif(command[0]=='2'):
        a.append(command[1])
    elif(command[0]=='3'):
        if(len(a)==0):
            print(-1)
        else:
            print(a.popleft())
    elif(command[0]=='4'):
        if(len(a)==0):
            print(-1)
        else:
            print(a.pop())
    elif(command[0]=='5'):
        print(len(a))
    elif(command[0]=='6'):
        if(len(a)==0):
            print(1)
        else:
            print(0)
    elif(command[0]=='7'):
        if(len(a)==0):
            print(-1)
        else:
            print(a[0])
    elif(command[0]=='8'):
        if(len(a)==0):
            print(-1)
        else:
            print(a[-1])