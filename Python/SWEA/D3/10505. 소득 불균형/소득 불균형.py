T=int(input())

for i in range(1,T+1):
    N=int(input())
    pay_list=list(map(int,input().split()))
    avg=sum(pay_list)/len(pay_list)
    count=0
    for pay in pay_list:
        if(pay<=avg):
            count+=1
    print(f'#{i} {count}')
