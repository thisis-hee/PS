import sys

input = sys.stdin.readline

num_list = [0]*2469123

for i in range(2,246913):
    is_prime = True
    for j in range(2, int(i**(1/2))+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        num_list[i]=1

while True:
    a=int(input())

    if a==0:
        break
    else:
        print(sum(num_list[a+1:2*a+1]))