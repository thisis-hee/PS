import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

N=int(input())
N_list=set(map(int,input().split()))

M=int(input())
M_list=list(map(int,input().split()))



for i in M_list:
    if(i in N_list):
        print(1)
    else:
        print(0)