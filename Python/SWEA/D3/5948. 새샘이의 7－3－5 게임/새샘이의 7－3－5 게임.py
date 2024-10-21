from itertools import combinations

T=int(input())

for i in range(1,T+1):
    num_list=list(map(int,input().split()))
    sum_list=set()
    for j in combinations(num_list,3):
        sum_list.add(sum(j))
    sum_list=sorted(list(sum_list), reverse=True)
    print(f'#{i} {sum_list[4]}')
    