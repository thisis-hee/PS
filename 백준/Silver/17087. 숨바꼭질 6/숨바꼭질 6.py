# 최대공약수 문제인 것을 인지한 것은 잘했음

# math 라이브러리 이용해서 쉽게 풀이 가능
import math

N,S = map(int,input().split())
K = list(map(int,input().split()))
D = []
for i in range(len(K)):
    D.append(abs(S-K[i]))
ans = D[0]
for i in D:
    # 최대공약수 구해주는 함수
    ans = math.gcd(i,ans)
print(ans)
