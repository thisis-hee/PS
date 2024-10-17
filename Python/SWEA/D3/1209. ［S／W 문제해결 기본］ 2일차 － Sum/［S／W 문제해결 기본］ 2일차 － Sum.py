for i in range(1,10+1):
    N=int(input())
    array=[]
    for _ in range(100):
        array.append(list(map(int,input().split())))
    
    max=0

    # 행 최대
    for j in range(100):
        if(sum(array[j])>max):
            max=sum(array[j])

    # 열 최대
    array_t=list(map(list,zip(*array)))
    for k in range(100):
        if(sum(array_t[k])>max):
            max=sum(array_t[k])
    
    # 대각선 최대
    line_sum1=0
    for l in range(100):
        line_sum1+=array[l][l]
    
    if(line_sum1>max):
        max=line_sum1
    
    # 대각선 최대
    line_sum2=0
    for m in range(100):
        line_sum2+=array[m][99-m]

    if(line_sum2>max):
        max=line_sum2
    
    print(f'#{i} {max}')