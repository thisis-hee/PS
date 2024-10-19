T=int(input())

for i in range(1,T+1):
    N=int(input())
    num_list=list(map(int,input().split()))
    avg_num=0
    for j in range(len(num_list)-2):
        if(num_list[j]<num_list[j+1]<num_list[j+2]):
            avg_num+=1
        elif(num_list[j]>num_list[j+1]>num_list[j+2]):
            avg_num+=1
    print(f'#{i} {avg_num}')

