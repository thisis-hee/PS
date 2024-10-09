N=int(input())

num_list=[1]
for i in range(N):
    num_list.append(num_list[i]*2)

print(*num_list)