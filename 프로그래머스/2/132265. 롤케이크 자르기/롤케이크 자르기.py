from collections import Counter

def solution(topping):
    answer = 0
    
    older=Counter(topping)
    younger={}
    
    for i in topping:
        if i in younger:
            younger[i]+=1
        else:
            younger[i]=1
        
        older[i]-=1
        
        if older[i]==0:
            del(older[i])
        
        if len(older)==len(younger):
            answer+=1
    
    return answer