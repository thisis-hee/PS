T=int(input())

for i in range(1,T+1):
    L,U,X=map(int,input().split())
    if(X<L):
        print(f'#{i} {L-X}')
    elif(L<X<=U):
        print(f'#{i} {0}')
    elif(X>U):
        print(f'#{i} {-1}')