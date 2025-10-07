def solution(s):
    answer=''
    
    s_list=s.split(' ')
    
    for i in s_list:
        for j in range(len(i)):
            if j%2==0:
                answer+=i[j].upper()
            else:
                answer+=i[j].lower()
        answer+=' '
            
    answer=answer[:-1]
    
    return answer