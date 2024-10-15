T=int(input())

for i in range(1,T+1):
    N,M=map(int,input().split())
    area=[]
    for _ in range(N):
        area.append(list(map(int,input().split())))
    max=0
    # 행 방향 반복
    for j in range(N-M+1):
        # 열 방향 반복
        for k in range(N-M+1):
            count=0
            for x in range(j,j+M):
                for y in range(k,k+M):
                    count+=area[x][y]
            if(count>max):
                max=count
    print(f'#{i} {max}')