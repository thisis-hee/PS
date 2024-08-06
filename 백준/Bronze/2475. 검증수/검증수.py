A=list(map(int,input().split()))
num=0
for i in range(len(A)):
    num+=A[i]**2

print(num%10)