# 슬라이싱 활용해 역순으로 바꿔주기
N,M=map(int,input().split(' '))
basket=list(range(1,N+1))
for _ in range(M):
    i,j=map(int,input().split(' '))
    basket[i-1:j]=basket[i-1:j][::-1]

print(*basket)
