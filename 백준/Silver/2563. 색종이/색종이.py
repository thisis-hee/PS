N=int(input())
row=100
col=100
count=0
arr = [[0 for j in range(col)] for i in range(row)]

for i in range(N):
    a, b = map(int,input().split(' '))
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j]=1

for i in range(row):
    for j in range(col):
        if(arr[i][j]==1):
            count+=1

print(count)