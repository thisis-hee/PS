n=int(input())

for i in range(1,n+1):
    print((n-i)*' '+(2*(i-1)+1)*'*')

for j in range(n,0,-1):
    print((n-j+1)*' '+(2*(j-2)+1)*'*')