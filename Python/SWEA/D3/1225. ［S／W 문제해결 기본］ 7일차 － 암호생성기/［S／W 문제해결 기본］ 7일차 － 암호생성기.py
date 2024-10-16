from collections import deque

for i in range(1, 10+1):
    a=int(input())
    num_list=deque(map(int,input().split()))
    cycle=0
    init=1
    while(True):
        num_list.append(num_list.popleft()-(init%6))
        init+=1
        if(init==6):
            init=1
            cycle+=1
 
        if(num_list[len(num_list)-1]<=0):
            break
    num_list[len(num_list)-1]=0
    print(f'#{i}', *num_list)
