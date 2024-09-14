T=int(input())


for _ in range(T):
    N=int(input())
    wear_dict={}

    for _ in range(N):
        a,b=input().split()
        wear_dict[a]=b
        

    value_count={}

    for value in wear_dict.values():
        if(value in value_count):
            value_count[value]+=1
        else:
            value_count[value]=1
        
    sum=1

    for count in value_count.values():
        sum*=(count+1)

    answer=sum-1
    print(answer)