B,C,D=map(int,input().split())

discount_num=min(B,C,D)

burger=sorted(list(map(int,input().split())),reverse=True)
side=sorted(list(map(int,input().split())),reverse=True)
drink=sorted(list(map(int,input().split())), reverse=True)

total=0

for price in burger:
    total+=price

for price in side:
    total+=price

for price in drink:
    total+=price

print(total)

for i in range(discount_num):
    burger[i]=0.9*burger[i]
    side[i]=0.9*side[i]
    drink[i]=0.9*drink[i]

discount_total=0

for price in burger:
    discount_total+=price

for price in side:
    discount_total+=price

for price in drink:
    discount_total+=price

print(int(discount_total))