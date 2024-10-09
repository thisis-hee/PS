T=int(input())

for i in range(1,T+1):
    A,B=map(int,input().split())
    A_list=list(map(int,input().split()))
    B_list=list(map(int,input().split()))
    sum_list=[]
    if(len(A_list)<len(B_list)):
        while(len(A_list)<=len(B_list)):
            sum=0
            for j in range(len(A_list)):
                sum+=A_list[j]*B_list[j]
            sum_list.append(sum)
            A_list.insert(0,0)
        print(f'#{i} {max(sum_list)}')
    else:
        while(len(A_list)>=len(B_list)):
            sum=0
            for j in range(len(B_list)):
                sum+=A_list[j]*B_list[j]
            sum_list.append(sum)
            B_list.insert(0,0)
        print(f'#{i} {max(sum_list)}')
