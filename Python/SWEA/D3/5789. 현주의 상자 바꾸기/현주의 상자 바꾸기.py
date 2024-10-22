
T=int(input())

for i in range(1,T+1):
    N,Q=map(int,input().split())
    box=[0 for _ in range(N)]
    for j in range(1,Q+1):
        L,R=map(int,input().split())
        box[L-1:R]=[j for _ in range(R-L+1)]
        
    print(f'#{i}', *box)