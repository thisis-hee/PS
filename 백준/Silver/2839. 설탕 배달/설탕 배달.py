import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

N=int(input())
cnt=0

while True:
    if(N%5==0):
        print((N//5)+cnt)
        break
    else:
        N=N-3
        cnt+=1

    if(N<0):
        print(-1)
        break