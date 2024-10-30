X=int(input())

n=1
while(True):
    if(n**2+n>=2*X):
        break
    else:
        n+=1

start=int(n*(n-1)/2)
a=1
if(n%2==1):
    for i in range(start, X-1):
        n-=1
        a+=1
    print(f'{n}/{a}')
else:
    for i in range(start, X-1):
        n-=1
        a+=1
    print(f'{a}/{n}')