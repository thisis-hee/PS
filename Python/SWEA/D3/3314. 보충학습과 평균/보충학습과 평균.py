T=int(input())

for i in range(1,T+1):
    score_list=list(map(int,input().split()))
    for j in range(len(score_list)):
        if(score_list[j]<=35):
            score_list[j]=40
    print(f'#{i} {int(sum(score_list)/len(score_list))}')