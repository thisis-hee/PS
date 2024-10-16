def multiply(n,m):
    if(m>0):
        return n*multiply(n,m-1)
    else:
        return 1

for i in range(1,11):
    a=int(input())
    N,M=map(int,input().split())
    print(f'#{i} {multiply(N,M)}')