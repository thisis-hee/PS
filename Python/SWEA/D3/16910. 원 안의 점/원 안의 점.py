T=int(input())

for i in range(1,T+1):
    N=int(input())
    count=0
    for j in range(-N,N+1):
        for k in range(-N,N+1):
            if(j**2+k**2<=N**2):
                count+=1
    print(f'#{i} {count}')