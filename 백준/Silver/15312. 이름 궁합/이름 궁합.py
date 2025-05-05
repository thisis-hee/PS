import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
import math

alp_dict={
    'A':3,'B':2,'C':1,'D':2,'E':3,
    'F':3,'G':2,'H':3,'I':3,'J':2,
    'K':2,'L':1,'M':2,'N':2,'O':1,
    'P':2,'Q':2,'R':2,'S':1,'T':2,
    'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1
}

A=input().rstrip()
B=input().rstrip()

num_list=[]

for i in range(len(A)):
    num_list.append(alp_dict[A[i]])
    num_list.append(alp_dict[B[i]])

while len(num_list)!=2:
    new_list=[]
    for i in range(len(num_list)-1):
        new_list.append((num_list[i]+num_list[i+1])%10)
    num_list=new_list

print(''.join(map(str,num_list)))