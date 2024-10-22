T=int(input())

for i in range(1,T+1):
    N=int(input())
    matrix=[]
    for _ in range(N):
        matrix.append(list(input().split()))
    
    matrix_90 = list(zip(*matrix[::-1]))
    
    matrix_180 = list(zip(*matrix_90[::-1]))
   
    matrix_270 = list(zip(*matrix_180[::-1]))

    print(f'#{i}')
    for k in range(len(matrix)):
        print(''.join(matrix_90[k]), ''.join(matrix_180[k]), ''.join(matrix_270[k]))