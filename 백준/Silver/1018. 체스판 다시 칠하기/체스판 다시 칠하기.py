import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
from collections import deque

N,M=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(N)]

a=['B','W','B','W','B','W','B','W']
b=['W','B','W','B','W','B','W','B']

ans1=[]
ans2=[]
cnt_list=[]

for i in range(8):
    if(i%2==0):
        ans1.append(a)
        ans2.append(b)
    else:
        ans1.append(b)
        ans2.append(a)

for i in range(N-8+1):
    for j in range(M-8+1):
        new_arr=[arr[x][j:j+8] for x in range(i,i+8)]
        cnt1=0
        cnt2=0
        for x in range(8):
            for y in range(8):
                if(new_arr[x][y]!=ans1[x][y]):
                    cnt1+=1
        for x in range(8):
            for y in range(8):
                if(new_arr[x][y]!=ans2[x][y]):
                    cnt2+=1
        cnt_list.append(cnt1)
        cnt_list.append(cnt2)

print(min(cnt_list))