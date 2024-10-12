T=int(input())

for i in range(1,T+1):
    N=int(input())
    drink=[('1/'+str(N)) for _ in range(N)]
    print(f'#{i}', *drink)