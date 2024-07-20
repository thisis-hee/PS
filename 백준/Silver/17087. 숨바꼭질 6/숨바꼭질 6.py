import math

N,S = map(int,input().split())
K = list(map(int,input().split()))
D = []
for i in range(len(K)):
    D.append(abs(S-K[i]))
ans = D[0]
for i in D:
    ans = math.gcd(i,ans)
print(ans)