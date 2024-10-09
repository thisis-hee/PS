T=int(input())
for j in range(1,T+1):
    num=int(input())
    new_num=num
    num_list=[]
    k=2
    while(True):
        number=list(str(new_num))
        for i in range(len(number)):
            if(number[i] not in num_list):
                num_list.append(number[i])
                num_list.sort()
        if(['0','1','2','3','4','5','6','7','8','9']==num_list):
            break
        else:
            new_num=num*k
            k+=1
    print(f'#{j} {num*(k-1)}')