date_dict={1:31,
           2:28,
           3:31,
           4:30,
           5:31,
           6:30,
           7:31,
           8:31,
           9:30,
           10:31,
           11:30,
           12:31}

T=int(input())

for i in range(1,T+1):
    A_M,A_D,B_M,B_D=map(int,input().split())
    if(A_M==B_M):
        print(f'#{i} {B_D-A_D+1}')
    else:
        num=B_M-A_M-1
        total_day=0
        for j in range(1,num+1):
            total_day+=date_dict[A_M+j]
        print(f'#{i} {total_day+date_dict[A_M]-A_D+B_D+1}')