N, digit=map(int,input().split())

num_list=[]

for i in range(1,N+1):
    i=str(i)
    for j in range(len(i)):
        num_list.append(i[j])

print(num_list.count(str(digit)))