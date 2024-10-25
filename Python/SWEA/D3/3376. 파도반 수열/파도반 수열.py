T=int(input())

for i in range(1,T+1):
    P=[1,1,1]
    for j in range(3,100):
        P.append(P[j-3]+P[j-2])
    N=int(input())
    print(f'#{i} {P[N-1]}')