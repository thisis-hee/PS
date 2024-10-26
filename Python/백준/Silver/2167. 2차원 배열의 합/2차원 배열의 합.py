N,M=map(int,input().split())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))

sum_matrix=[[0 for _ in range(M+1)] for _ in range(N+1)]

for row in range(1,len(sum_matrix)):
    for col in range(1,len(sum_matrix[0])):
        sum_matrix[row][col]=sum_matrix[row-1][col]+sum_matrix[row][col-1]-sum_matrix[row-1][col-1]+matrix[row-1][col-1]

K=int(input())
for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    print(sum_matrix[x2][y2]-sum_matrix[x1-1][y2]-sum_matrix[x2][y1-1]+sum_matrix[x1-1][y1-1])