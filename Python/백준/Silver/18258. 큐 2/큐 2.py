from collections import deque
import sys

N=int(sys.stdin.readline())

num_list=deque()

for _ in range(N):
    method=list(sys.stdin.readline().rstrip().split())
    
    if(method[0]=='push'):
        num_list.append(int(method[1]))
    elif(method[0]=='pop'):
        if(len(num_list)!=0):
            print(num_list.popleft())
        else:
            print(-1)
    elif(method[0]=='size'):
        print(len(num_list))
    elif(method[0]=='empty'):
        if(len(num_list)!=0):
            print(0)
        else:
            print(1)
    elif(method[0]=='front'):
        if(len(num_list)!=0):
            print(num_list[0])
        else:
            print(-1)
    elif(method[0]=='back'):
        if(len(num_list)!=0):
            print(num_list[len(num_list)-1])
        else:
            print(-1)