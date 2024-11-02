import sys

input = sys.stdin.readline

S=int(input())

n=1
while True:
    if(n*(n+1)/2>S):
        break
    else:
        n+=1
print(n-1)