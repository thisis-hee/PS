M=int(input())
N=int(input())
sum=0
num_list=[]
for i in range(M,N+1):
    count=0
    for j in range(1,i):
        if(i%j==0):
            count+=1
    if(count==1):
        num_list.append(i)

if(num_list==[]):
    print(-1)
else:
    for i in num_list:
        sum+=i

    print(sum)
    print(num_list[0])