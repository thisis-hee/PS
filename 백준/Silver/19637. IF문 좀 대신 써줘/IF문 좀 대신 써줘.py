import sys
input=sys.stdin.readline

N,M=map(int,input().split())

power_list=[]

for _ in range(N):
    a,b=input().split()
    power_list.append((a,int(b)))

check_list=[]

for _ in range(M):
    start=0
    end=N-1
    target=int(input())
    answer=''

    while start<=end:
        mid=(start+end)//2

        if(target<=power_list[mid][1]):
            end=mid-1
            answer=power_list[mid][0]
        else:
            start=mid+1
            answer=power_list[start][0]
    print(answer)
