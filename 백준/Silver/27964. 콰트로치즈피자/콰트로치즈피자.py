N=int(input())

topping_list=set(input().split())

count=0
for topping in topping_list:
    if(topping[-6:]=="Cheese"):
        count+=1

if(count>=4):
    print("yummy")
else:
    print("sad")