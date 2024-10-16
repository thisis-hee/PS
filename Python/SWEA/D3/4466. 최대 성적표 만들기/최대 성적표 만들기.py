T=int(input())

for i in range(1,T+1):
    N,K=map(int,input().split())
    score=list(map(int,input().split()))
    score.sort(reverse=True)
    print(f'#{i} {sum(score[0:K])}')
