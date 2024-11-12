import sys
input=sys.stdin.readline

N=int(input())
num=[0]*10001

for _ in range(N):
    num[int(input())]+=1

for j in range(len(num)):
    if(num[j]!=0):
        for _ in range(num[j]):
            print(j)