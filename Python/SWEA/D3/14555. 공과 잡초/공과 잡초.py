
T=int(input())

for i in range(1,T+1):
    ball=list(input())
    count=0
    for j in range(len(ball)-1):
        if(ball[j]+ball[j+1]=='()' or ball[j]+ball[j+1]=='|)' or ball[j]+ball[j+1]=='(|'):
            count+=1
    print(f'#{i} {count}')