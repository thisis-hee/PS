T=int(input())

for _ in range(T):
    a=list(map(int,input().split()))
    a.sort()
    print(a[7])