for i in range(1,11):
    length,num=map(int,input().split())
    num=list(str(num))
    j=0
    while(True):
        try:
            if(num[j]==num[j+1]):
                del num[j:j+2]
                j=0
                continue
            j+=1
        # 예외처리로 while문 탈출
        except:
            break
    # 앞자리가 0인경우 제거
    if(num[0]=='0'):
        num=num[1:len(num)]
    print(f'#{i}', ''.join(num))
