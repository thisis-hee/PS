import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

N=int(input())

fib=[0,1]

for i in range(N-2):
    fib.append(fib[i]+fib[i+1])

print(fib[N-2]+fib[N-1])