# 가장 작은 약수, 가장 큰 약수의 곱이 곧 답이 됨.
N=int(input())

A=list(map(int,input().split()))
A.sort()
print(A[0]*A[-1])
