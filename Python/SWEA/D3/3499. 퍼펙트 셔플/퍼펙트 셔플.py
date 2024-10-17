T=int(input())

for i in range(1,T+1):
    N=int(input())
    card_list=list(input().split())

    shuffle_list=[]
    if(N%2==0):
        a_list=card_list[:len(card_list)//2]
        b_list=card_list[len(card_list)//2:]
        for j in range(len(card_list)//2):
            shuffle_list.append(a_list[j])
            shuffle_list.append(b_list[j])
        print(f'#{i}', *shuffle_list)
    else:
        a_list=card_list[:len(card_list)//2+1]
        b_list=card_list[len(card_list)//2+1:]
        for j in range(len(card_list)//2):
            shuffle_list.append(a_list[j])
            shuffle_list.append(b_list[j])
        shuffle_list.append(a_list[len(a_list)-1])
        print(f'#{i}', *shuffle_list)