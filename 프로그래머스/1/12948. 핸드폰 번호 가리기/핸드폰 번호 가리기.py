def solution(phone_number):
    answer=[]
    
    for i in range(len(phone_number[0:-4])):
        answer.append('*')
        
    for i in phone_number[-4:]:
        answer.append(i)
    
    answer=''.join(answer)
    
    return answer