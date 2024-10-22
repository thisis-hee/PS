
T=int(input())

for i in range(1,T+1):
    num_list=list(input())
    init_list=['0' for _ in range(len(num_list))]
    j=0
    count=0
    while(True):
        try:
            if(num_list[j]!=init_list[j]):
                init_list[j:]=[num_list[j] for _ in range(len(init_list[j:]))]
                count+=1
                j+=1
            else:
                j+=1
                continue
        except:
            break
    print(f'#{i} {count}')