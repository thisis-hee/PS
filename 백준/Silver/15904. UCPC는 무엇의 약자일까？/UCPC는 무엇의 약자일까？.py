import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

s=input()
ans=[]

for i in range(len(s)):
    if(len(ans)==0 and s[i]=='U'):
        ans.append(s[i])
        continue
    elif(len(ans)==1 and s[i]=='C'):
        ans.append(s[i])
        continue
    elif(len(ans)==2 and s[i]=='P'):
        ans.append(s[i])
        continue
    elif(len(ans)==3 and s[i]=='C'):
        ans.append(s[i])
        break

if(len(ans)==4):
    print("I love UCPC")
else:
    print("I hate UCPC")
