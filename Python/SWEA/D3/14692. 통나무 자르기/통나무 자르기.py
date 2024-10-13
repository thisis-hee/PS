T=int(input())

for i in range(1,T+1):
    length=int(input())
    if(length%2==0):
        print(f'#{i} Alice')
    else:
        print(f'#{i} Bob')