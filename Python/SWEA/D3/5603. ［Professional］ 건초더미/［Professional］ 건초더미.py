# min, max로 풀면 시간초과. 평균으로 풀어야 함
T=int(input())

for i in range(1,T+1):
    N=int(input())
    dummy=[]
    for _ in range(N):
        dummy.append(int(input()))
    
    avg=sum(dummy)/len(dummy)
    
    correct=0

    for j in range(N):
        correct+=abs(dummy[j]-avg)
    
    print(f'#{i} {int(correct/2)}')
