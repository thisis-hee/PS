import sys

input = sys.stdin.readline

N,M=map(int,input().split())
num_list=list(map(int,input().split()))

sum=[0]
tmp=0

for i in num_list:
    tmp=tmp+i
    sum.append(tmp)

for _ in range(M):
    a,b=map(int,input().split())
    print(sum[b]-sum[a-1])