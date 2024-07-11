N=int(input())
row=100
col=100
count=0

# 0으로 채워진 2차원 배열 생성
arr = [[0 for j in range(col)] for i in range(row)]

for i in range(N):
    a, b = map(int,input().split(' '))
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j]=1

# 2차원 배열은 sum(arr) 안됨. 그래서 for문으로 진행
for i in range(row):
    for j in range(col):
        if(arr[i][j]==1):
            count+=1

print(count)
