
T=int(input())

basic=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for i in range(1,T+1):
    N,K=map(int,input().split())
    grade=[]

    for aaa in basic:
        for _ in range(N//10):
            grade.append(aaa)
            
    score=[]
    for _ in range(N):
        score.append(list(map(int,input().split())))
    total=[]
    for j in range(len(score)):
        total.append(0.35*score[j][0]+0.45*score[j][1]+0.2*score[j][2])
    sorted_total=sorted(total,reverse=True)
    print(f'#{i} {grade[sorted_total.index(total[K-1])]}')