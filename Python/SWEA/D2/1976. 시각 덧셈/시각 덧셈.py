T=int(input())

for i in range(1,T+1):
    h1,m1,h2,m2=map(int,input().split())
    if(m1+m2>=60):
        m=(m1+m2)%60
        h=1
    else:
        h=0
        m=m1+m2
    
    if(h1+h2+h>=13):
        real_h=(h1+h2+h)%13+1
    else:
        real_h=h1+h2+h
    
    print(f'#{i} {real_h} {m}')