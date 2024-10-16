T=int(input())

for i in range(1,T+1):
    N=int(input())
    area=[]
    for _ in range(N):
        area.append(list(input()))
    
    total=0

    for row in range(N//2+1):
        value=area[row][N//2-row:N//2+row+1]
        for j in range(len(value)):
            total+=int(value[j])
            
    for row in range(N//2+1,N):
        value=area[row][row-N//2:N-(row-N//2)]
        for j in range(len(value)):
            total+=int(value[j])
    print(f'#{i} {total}')

