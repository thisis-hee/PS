
T=int(input())

for i in range(1,T+1):
    line_list=list(map(int,input().split()))
    if(len(set(line_list))==1):
        print(f'#{i} {line_list[0]}')
    else:
        line_dict={}
        for j in line_list:
            if(j not in line_dict):
                line_dict[j]=1
            else:
                line_dict[j]+=1
        print(f'#{i}', *[key for key, value in line_dict.items() if value==1])
