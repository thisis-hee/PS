def solution(k, tangerine):
    answer = 0
    
    a=dict()
    
    for i in tangerine:
        if i in a.keys():
            a[i]+=1
        else:
            a[i]=1
    
    result = sorted(a.values(), reverse=True)
    real_answer=0
    for i in result:
        answer+=i
        real_answer+=1
        if(answer>=k):
            break
    
    return real_answer