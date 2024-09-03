T=int(input())

for i in range(1,T+1):
    score_list=list(map(int,input().split()))
    max_score=max(score_list[1:])
    min_score=min(score_list[1:])
    sort_score=sorted(score_list[1:],reverse=True)

    max_gap=0
    for j in range(len(sort_score)-1):
        if(sort_score[j]-sort_score[j+1]>max_gap):
            max_gap=sort_score[j]-sort_score[j+1]

    print(f'Class {i}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {max_gap}')