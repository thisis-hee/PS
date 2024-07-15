# 에라토스테네스의 체 활용

M,N=map(int,input().split())

for i in range(M,N+1):
    if(i==1):
        continue
    # 제곱근까지만 확인하면 됨
    for j in range(2, int(i**(1/2))+1):
        if(i%j==0):
            break
    else:
        print(i)
