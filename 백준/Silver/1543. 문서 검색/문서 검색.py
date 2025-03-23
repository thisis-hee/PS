import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations

s1=input().rstrip()
s2=input().rstrip()
s1_len=len(s1)
s2_len=len(s2)
cnt=0
i=0

while True:
    if(i>s1_len):
        break

    if(s1[i:i+s2_len]==s2):
        cnt+=1
        s1=s1[i+s2_len:]
        i=0
    else:
        i+=1
print(cnt)