N=int(input())
sum=3
if(N==1):
    print(9)
else:
    for i in range(1,N):
        sum+=2**i
    print(sum**2)
