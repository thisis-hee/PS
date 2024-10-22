
T=int(input())

for i in range(1,T+1):
    N,A,B=map(int,input().split())
    if(N-A-B>=0):
        mini=0
        print(f'#{i} {min(A,B)} {mini}')
    else:
        print(f'#{i} {min(A,B)} {abs(N-A-B)}')