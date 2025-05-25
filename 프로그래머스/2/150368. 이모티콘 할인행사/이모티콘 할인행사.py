from itertools import product

def solution(users, emoticons):
    # 할인율
    sales_rate=[10,20,30,40]
    
    # 모든 할인에 따른 경우의 수를 저장할 리스트
    ans_list=[]
    
    # itertools의 product를 이용해서 모든 할인율 경우의 수를 체크 최대 4**7임.
    for i in product(sales_rate, repeat=len(emoticons)):
        emoticon_plus_cnt=0
        total_price=0
        price_list=[]
        
        # 할인된 이모티콘 가격 계산
        for j in range(len(emoticons)):
            price_list.append((100-i[j])*emoticons[j]*0.01)
        
        # user 돌면서 이모티콘 플러스 여부와 구매 금액 체크
        for k in range(len(users)):
            users_price=0
            
            # 이모티콘 돌면서
            for l in range(len(emoticons)):
                # 할인율이 user가 원하는 할인율보다 크면
                if(i[l]>=users[k][0]):
                    # 유저의 가격에 할인된 가격을 더하기
                    users_price+=price_list[l]
            
            # 만약 이모티콘 플러스를 구매할 상한가를 users_price가 넘으면
            if(users_price>=users[k][1]):
                # 이모티콘 구매를 취소하고, (users_price=0) 
                users_price=0
                # 이모티콘 플러스 카운트를 1 증가시킴
                emoticon_plus_cnt+=1
            # 상한가를 못넘은 경우에는 total_price에 users_price를 더해줌
            total_price+=users_price
        # 정답 리스트에 리스트로 넣어줌
        ans_list.append([emoticon_plus_cnt, total_price])
    
    # 람다식을 활용해 정렬 순서를 맞춰줌
    ans_list.sort(key=lambda x:[x[0], x[1]], reverse=True)
    answer = ans_list[0]
    return answer