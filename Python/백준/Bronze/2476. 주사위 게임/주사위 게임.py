import sys

input = sys.stdin.readline

N=int(input())

prize=[]

dice_list=[]
for _ in range(N):
    a=list(map(int,input().split()))
    dice_list.append(a)

for i in range(len(dice_list)):
    if(len(set(dice_list[i]))==1):
        prize.append(10000+(dice_list[i][0])*1000)
    elif(len(set(dice_list[i]))==3):
        prize.append(max(dice_list[i])*100)
    else:
        if(dice_list[i].count(dice_list[i][0])==2):
            prize.append(1000+dice_list[i][0]*100)
        else:
            prize.append(1000+dice_list[i][1]*100)

print(max(prize))