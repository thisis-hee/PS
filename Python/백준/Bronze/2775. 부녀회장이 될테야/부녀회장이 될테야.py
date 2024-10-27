T=int(input())

for _ in range(T):
    k=int(input())
    n=int(input())
    matrix=[[i for i in range(n+1)]]
    for _ in range(k):
        matrix.append([0]*(n+1))
    
    for row in range(1,k+1):
        for ho in range(1,n+1):
            matrix[row][ho]=sum(matrix[row-1][1:ho+1])
    print(matrix[k][n])