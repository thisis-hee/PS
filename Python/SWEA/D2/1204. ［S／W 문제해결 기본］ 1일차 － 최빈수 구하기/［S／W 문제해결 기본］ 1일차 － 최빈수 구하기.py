T=int(input())

for i in range(1,T+1):
    N=int(input())
    num_dict={}
    num_list=list(map(int,input().split()))
    
    for j in range(len(num_list)):
        if(num_list[j] not in num_dict.keys()):
            num_dict[num_list[j]]=1
        else:
            num_dict[num_list[j]]+=1
    # key=num_dict.get 기억
    max_key = max(num_dict, key=num_dict.get)
    
    print(f'#{i} {max_key}')
