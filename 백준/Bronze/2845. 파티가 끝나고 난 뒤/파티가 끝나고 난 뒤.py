L,P=map(int,input().split())

num_list=list(map(int,input().split()))

for i in range(len(num_list)):
    num_list[i]-=L*P

print(*num_list)