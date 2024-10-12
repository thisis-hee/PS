T=int(input())

for i in range(1,T+1):
    count_50000=0
    count_10000=0
    count_5000=0
    count_1000=0
    count_500=0
    count_100=0
    count_50=0
    count_10=0
    N=int(input())
    if(N>=50000):
        count_50000=N//50000
        N=N-count_50000*50000
    if(N>=10000):
        count_10000=N//10000
        N=N-count_10000*10000
    if(N>=5000):
        count_5000=N//5000
        N=N-count_5000*5000
    if(N>=1000):
        count_1000=N//1000
        N=N-count_1000*1000
    if(N>=500):
        count_500=N//500
        N=N-count_500*500
    if(N>=100):
        count_100=N//100
        N=N-count_100*100
    if(N>=50):
        count_50=N//50
        N=N-count_50*50
    if(N>=10):
        count_10=N//10
        N=N-count_10*10
    
    print(f'#{i}')
    print(f'{count_50000} {count_10000} {count_5000} {count_1000} {count_500} {count_100} {count_50} {count_10}')
