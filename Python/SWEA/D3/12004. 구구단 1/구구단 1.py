T=int(input())

num_list=[i for i in range(1,10)]

all=[]

for j in num_list:
    for k in num_list:
        if(j*k not in all):
            all.append(j*k)

for j in range(1,T+1):
    if(int(input()) not in all):
        print(f'#{j} No')
    else:
        print(f'#{j} Yes')