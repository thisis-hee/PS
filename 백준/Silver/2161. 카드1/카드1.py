from collections import deque

N=int(input())
num_list=deque(range(1,N+1))
card_list=[]


i=0
while(True):
    card_list.append(num_list.popleft())
    print(card_list[i])
    if(len(num_list)==0):
        break
    num_list.append(num_list.popleft())
    i+=1