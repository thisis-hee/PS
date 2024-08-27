T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    count=0
    for i in range(N,M+1):
        i=list(str(i))
        for j in range(len(i)):
            if(i[j]=='0'):
                count+=1
    print(count)