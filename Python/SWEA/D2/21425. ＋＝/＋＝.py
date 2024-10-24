
T=int(input())

for i in range(1,T+1):
    A,B,N=map(int,input().split())
    count=1
    while(True):
        if(A+B>N):
            break
        if(A>B):
            B+=A
            count+=1
        else:
            A+=B
            count+=1
    print(count)  