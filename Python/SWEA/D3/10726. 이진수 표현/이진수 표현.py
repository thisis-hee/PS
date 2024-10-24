T=int(input())

for i in range(1,T+1):
    N,M=map(int,input().split())
    if(M%(2**N)==(2**N)-1):
        print(f'#{i} ON')
    else:
        print(f'#{i} OFF')
