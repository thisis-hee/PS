T=int(input())

for i in range(1,T+1):
    N=int(input())
    prime=[]
    for j in range(1,int(N**(0.5))+1):
        if(N%j==0):
            prime.append(j)
    
    print(f'#{i} {N//prime[len(prime)-1]-1+prime[len(prime)-1]-1}')
    