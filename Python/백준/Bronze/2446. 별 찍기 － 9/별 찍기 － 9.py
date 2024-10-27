n=int(input())

for i in range(1,n):
    print(' '*(i-1)+'*'*(2*(n-i)+1))

for j in range(1,n+1):
    print(' '*(n-j)+'*'*(2*j-1))