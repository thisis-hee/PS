# factorial로 계산해서 풀면 시간초과 뜸.
# 2의 지수와 5의 지수를 이용해서 풀어야 함.
# ex) 2*5 하나씩 있으면 끝자리가 0, 2*2*5*5 두개씩 있으면 끝자리가 00 이런 규칙.

n,m=map(int,input().split())

def count2(N):
    if(N<2):
        return 0
    
    count=0
    while(N>=2):
        count+=N//2
        N=N//2
    return count

def count5(N):
    if(N<5):
        return 0
    
    count=0
    while(N>=5):
        count+=N//5
        N=N//5
    return count

two_count=count2(n)-count2(n-m)-count2(m)
five_count=count5(n)-count5(n-m)-count5(m)
print(min(two_count,five_count))
