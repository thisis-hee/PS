T=int(input())

for i in range(1,T+1):
    N,K=map(int,input().split())
    num_list=list(map(int,input().split()))
    no_check_list=[]
    for num in range(1,N+1):
        if(num not in num_list):
            no_check_list.append(num)
    print(f"#{i}", end=' ')
    print(*no_check_list)