T=int(input())

for i in range(1,T+1):
    num_list=list(map(int,input().split()))
    num_list.sort()
    new_list=num_list[1:9]
    print(f'#{i} {int(round(sum(new_list)/len(new_list),0))}')