
T=int(input())

for i in range(1,T+1):
    N,M=map(int,input().split())
    N_list=list(input().split())
    M_list=list(input().split())

    Q=int(input())
    word_list=[]
    for _ in range(Q):
        year=int(input())
        if(year%N==0 and year%M==0):
            word_list.append(N_list[len(N_list)-1]+M_list[len(M_list)-1])
        elif(year%N==0 and year%M!=0):
            word_list.append(N_list[len(N_list)-1]+M_list[year%(len(M_list))-1])
        elif(year%N!=0 and year%M==0):
            word_list.append(N_list[year%(len(N_list))-1]+M_list[len(M_list)-1])
        else:
            word_list.append(N_list[year%(len(N_list))-1]+M_list[(year%len(M_list))-1])
        
    print(f'#{i}', *word_list)