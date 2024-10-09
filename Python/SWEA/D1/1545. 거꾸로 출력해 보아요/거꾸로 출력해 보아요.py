N=int(input())

num_list=sorted([i for i in range(N+1)], reverse=True)
print(*num_list)
