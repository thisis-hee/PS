import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
import math

s=input().rstrip()

new=list(s.split(':'))
new=list(map(int,new))
gcd=math.gcd(new[0],new[1])

for i in range(len(new)):
    new[i]=int(new[i]/gcd)

print(':'.join(map(str,new)))