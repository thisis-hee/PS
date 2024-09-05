num_list=[]
i=1

while(True):
    for i in range(1,50):
        for _ in range(i):
            num_list.append(i)
    if(len(num_list)>=1000):
        break

A,B=map(int,input().split())

print(sum(num_list[A-1:B]))