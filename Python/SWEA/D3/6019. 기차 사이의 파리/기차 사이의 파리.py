T=int(input())

for i in range(1,T+1):
    D,A,B,F=map(int,input().split())
    print(f'#{i} {(F*D)/(A+B)}')