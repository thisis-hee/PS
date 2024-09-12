N=int(input())

card_num=set(map(int,input().split()))

M=int(input())
check_num=list(map(int,input().split()))

check_list=[]

for i in check_num:
    if(i in card_num):
        check_list.append(1)
    else:
        check_list.append(0)

print(*check_list)