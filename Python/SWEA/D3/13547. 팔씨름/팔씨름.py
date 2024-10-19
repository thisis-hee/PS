T=int(input())

for i in range(1,T+1):
    word=list(input())
    if(word.count('x')>=8):
        print(f'#{i} NO')
    else:
        print(f'#{i} YES')

