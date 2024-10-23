T=int(input())

for i in range(1,T+1):
    N,K=map(int,input().split())
    matrix=[list(input().split()) for _ in range(N)]
    matrix_t=list(map(list,zip(*matrix)))

    count=0

    new_matrix=[]
    for j in range(len(matrix)):
        new_matrix.append(''.join(matrix[j]))
    
    for k in range(len(new_matrix)):
        for l in range(len(new_matrix[k].split('0'))):
            if(new_matrix[k].split('0')[l]=='1'*K):
                count+=1
    
    new_matrix_t=[]
    for j in range(len(matrix_t)):
        new_matrix_t.append(''.join(matrix_t[j]))
    
    for k in range(len(new_matrix_t)):
        for l in range(len(new_matrix_t[k].split('0'))):
            if(new_matrix_t[k].split('0')[l]=='1'*K):
                count+=1
    
    print(f'#{i} {count}')