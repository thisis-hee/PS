A,B=map(int,input().split())

# 최대공약수
for i in range(1,min(A,B)+1):
    if(A%i==0 and B%i==0):
        gcd=i

# 최소공배수
# 최소공배수 공식 : 두 수의 곱 / 최대공약수 
lcm=(A*B)/gcd

print(gcd)
print(int(lcm))
