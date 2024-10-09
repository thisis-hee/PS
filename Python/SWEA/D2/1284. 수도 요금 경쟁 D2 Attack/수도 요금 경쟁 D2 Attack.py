T=int(input())
for i in range(1,T+1):
    P,Q,R,S,W=map(int,input().split())
    if(W<R):
        if(P*W>Q):
            print(f'#{i} {Q}')
        else:
            print(f'#{i} {P*W}')
    else:
        if(P*W>Q+S*(W-R)):
            print(f'#{i} {Q+S*(W-R)}')
        else:
            print(f'#{i} {P*W}')