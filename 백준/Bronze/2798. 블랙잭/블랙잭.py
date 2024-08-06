# 3중첩 for문
N,M=map(int,input().split())
A=list(map(int,input().split()))

result=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum=A[i]+A[j]+A[k]
            if(sum>M):
                continue
            else:
                result=max(result,sum)
                
print(result)


'''
# itertools 활용
from itertools import combinations

N,M=map(int,input().split())
A=list(map(int,input().split()))
s=[]

for i in combinations(A, 3):
    if(sum(i)>M):
        continue
    else:
        s.append(sum(i))

print(max(s))
'''
