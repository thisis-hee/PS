for i in range(1,10+1):
    N=int(input())
    height=list(map(int,input().split()))
    count=0
    for j in range(2,N-2):
        if(max(height[j-2],height[j-1],height[j],height[j+1],height[j+2])!=height[j]):
            continue
        else:
            count+=height[j]-max(height[j-2],height[j-1],height[j+1],height[j+2])

    print(f'#{i} {count}')