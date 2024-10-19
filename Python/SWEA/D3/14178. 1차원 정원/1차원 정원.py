T=int(input())

for i in range(1,T+1):
    N,D=map(int,input().split())
    if(N%(2*D+1)==0):
        print(f'#{i} {N//(2*D+1)}')
    else:
        print(f'#{i} {N//(2*D+1)+1}')
