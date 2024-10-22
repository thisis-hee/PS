
T=int(input())

for i in range(1,T+1):
    S=list(input())
    S3=[]
    for j in range(len(S)//3):
        S3.append(''.join(S[3*j:3*j+3]))
    
    if(len(S3)!=len(set(S3))):
        print(f'#{i} ERROR')
    else:
        s=13
        d=13
        h=13
        c=13
        for k in range(len(S3)):
            if(S3[k][0]=='S'):
                s-=1
            elif(S3[k][0]=='D'):
                d-=1
            elif(S3[k][0]=='H'):
                h-=1
            elif(S3[k][0]=='C'):
                c-=1
        print(f'#{i} {s} {d} {h} {c}')
