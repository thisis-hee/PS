
T=int(input())

for i in range(1,T+1):
    D,H,M=map(int,input().split())
    if(D<11 or (D==11 and H<11) or (D==1 and H==11 and M<11)):
        print(f'#{i} -1')
    else:
        if(M<11):
            H-=1
            M=M+60-11
        else:
            M=M-11

        if(H<11):
            D-=1
            H=H+24-11
        else:
            H=H-11
        
        D-=11
        print(f'#{i} {D*24*60+H*60+M}')
