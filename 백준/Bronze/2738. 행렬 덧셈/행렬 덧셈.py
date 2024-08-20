N,M=map(int,input().split())

a=[]
b=[]


for row in range(N):
    row=list(map(int,input().split()))
    a.append(row)

for col in range(N):
    col=list(map(int,input().split()))
    b.append(col)

for row in range(N):
    for col in range(M):
        print(a[row][col]+b[row][col], end=' ')
    print()