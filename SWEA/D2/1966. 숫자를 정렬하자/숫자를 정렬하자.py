T=int(input())

for i in range(1,T+1):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    print(f'#{i}', end=' ')
    for j in range(len(A)):
        print(A[j], end=' ')
    print()