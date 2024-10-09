T=int(input())

for i in range(T):
    num_list=list(map(int,input().split()))
    sum=0
    for j in range(len(num_list)):
        if(num_list[j]%2==1):
            sum+=num_list[j]
    print(f'#{i+1} {sum}')