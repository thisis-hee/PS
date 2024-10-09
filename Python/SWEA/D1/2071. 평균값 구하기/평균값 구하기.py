T=int(input())

for i in range(T):
    num_list=list(map(int,input().split()))
    print(f'#{i+1} {int(round(sum(num_list)/len(num_list),0))}')
