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
        except:
            break
    if(num[0]=='0'):
        num=num[1:len(num)]
    print(f'#{i}', ''.join(num))