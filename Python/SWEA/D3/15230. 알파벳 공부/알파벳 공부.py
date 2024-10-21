
T=int(input())

word='abcdefghijklmnopqrstuvwxyz'
for i in range(1,T+1):
    count=0
    check=input()
    j=0

    while(True):
        if(word[j]==check[j]):
            count+=1
            j+=1
            if(j>=min(len(word),len(check))):
                break
        else:
            break
    print(f'#{i} {count}')