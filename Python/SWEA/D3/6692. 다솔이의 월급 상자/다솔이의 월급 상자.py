T=int(input())


for i in range(1,T+1):
    N=int(input())
    avg=0
    for j in range(N):
        p,x=map(float,input().split())
        avg+=p*x
    print(f'#{i} {avg}')