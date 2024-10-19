for i in range(1,11):
    # 원본 암호문 길이
    length=int(input())
    
    # 원본 암호문 입력
    password=list(map(int,input().split()))

    # 명령어 수
    N=int(input())

    # 전체 명령어
    order=list(input().split())

    for j in range(len(order)):
        if(order[j]=='I'):
            for k in range(int(order[j+2])):
                password.insert(int(order[j+1])+k, int(order[j+3+k]))
        
        if(order[j]=='D'):
            del password[int(order[j+1]):int(order[j+1])+int(order[j+2])]

    
    print(f'#{i}', *password[0:10])