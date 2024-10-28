T=int(input())

for i in range(1,T+1):
    D,L,N=map(int,input().split())
    print(f'#{i} {int(N*D+D*(N*(N-1))*0.5*L*0.01)}')