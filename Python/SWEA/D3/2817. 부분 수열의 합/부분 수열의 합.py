from itertools import combinations

T=int(input())

for i in range(1,T+1):
    N,K=map(int,input().split())
    num_list=list(map(int,input().split()))
    count=0
    for j in range(1,N+1):
        for k in combinations(num_list,j):
            if(sum(k)==K):
                count+=1
    print(f'#{i} {count}')