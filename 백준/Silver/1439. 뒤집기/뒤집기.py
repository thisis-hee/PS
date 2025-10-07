import sys
from itertools import combinations

input = sys.stdin.readline

stack = []

word = input().rstrip()

for i in word:
    if not stack:
        stack.append(i)
    else:
        if stack[-1]!=i:
            stack.append(i)

if len(stack)==1:
    print(0)
else:
    print(len(stack)//2)