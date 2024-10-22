for i in range(1,10+1):
    dump=int(input())
    floor=list(map(int,input().split()))
    
    for _ in range(dump):
        floor[floor.index(max(floor))]-=1
        floor[floor.index(min(floor))]+=1
    
    print(f'#{i} {max(floor)-min(floor)}')
