for i in range(1,10+1):
    N=int(input())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    matrix_t=list(map(list,zip(*matrix)))
    count=0
    for row in range(100):
        stack=[]
        for j in range(100):
            if(stack==[] and matrix_t[row][j]==1):
                stack.append(matrix_t[row][j])
            elif(stack==[1] and matrix_t[row][j]==2):
                stack.append(matrix_t[row][j])
                stack.clear()
                count+=1
            else:
                continue
    print(f'#{i} {count}')