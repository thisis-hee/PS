import sys
input=sys.stdin.readline

N=int(input())
kilo=list(map(int,input().split()))
oil_price=list(map(int,input().split()))
total_price=0
current_price=oil_price[0]

for i in range(len(kilo)):
    if(current_price>=oil_price[i+1]):
        total_price+=current_price*kilo[i]
        current_price=oil_price[i+1]
    else:
        total_price+=current_price*kilo[i]

print(total_price)
