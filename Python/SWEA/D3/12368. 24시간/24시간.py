T=int(input())

for i in range(1,T+1):
    A,B=map(int,input().split())
    if(A+B<24):
        print(f'#{i} {A+B}')
    else:
        print(f'#{i} {(A+B)%24}')