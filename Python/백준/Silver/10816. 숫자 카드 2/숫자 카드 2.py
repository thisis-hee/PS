import sys
from collections import deque
input = sys.stdin.readline

N=int(input())
card_dict={}
card_list=list(map(int,input().split()))

for i in range(len(card_list)):
    if(card_list[i] in card_dict.keys()):
        card_dict[card_list[i]]+=1
    else:
        card_dict[card_list[i]]=1

M=int(input())
check_list=list(map(int,input().split()))

for j in range(len(check_list)):
    if(check_list[j] in card_dict.keys()):
        pass
    else:
        card_dict[check_list[j]]=0

for j in range(len(check_list)):
    print(card_dict[check_list[j]], end=' ')