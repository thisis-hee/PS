from collections import deque
import sys

N=int(sys.stdin.readline())

num_list=deque()

for _ in range(N):
    method=list(sys.stdin.readline().rstrip().split())
    
    if(method[0]=='1'):
        num_list.append(int(method[1]))
    elif(method[0]=='2'):
        if(len(num_list)!=0):
            print(num_list.pop())
        else:
            print(-1)
    elif(method[0]=='3'):
        print(len(num_list))
    elif(method[0]=='4'):
        if(len(num_list)!=0):
            print(0)
        else:
            print(1)
    elif(method[0]=='5'):
        if(len(num_list)!=0):
            print(num_list[len(num_list)-1])
        else:
            print(-1)