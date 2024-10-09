N=int(input())

num_list=[1]
for i in range(2,N+1):
    if(N%i==0):
        num_list.append(i)
print(*num_list)