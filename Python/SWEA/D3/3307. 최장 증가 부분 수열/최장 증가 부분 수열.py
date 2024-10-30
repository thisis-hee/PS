T=int(input())

for i in range(1,T+1):
    n=int(input())
    num_list=list(map(int,input().split()))
    dp=[1]*n
    for j in range(n):
        for k in range(j):
            if num_list[j] > num_list[k]:
                dp[j] = max(dp[j], dp[k] + 1)
    print(f'#{i} {max(dp)}')
