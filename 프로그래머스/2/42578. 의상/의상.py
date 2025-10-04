def solution(clothes):
    answer = 1
    
    kind = [x[1] for x in clothes]
    kind_dict = dict()
    
    for i in kind:
        if i not in kind_dict.keys():
            kind_dict[i]=1
        else:
            kind_dict[i]+=1
    
    a=[*kind_dict.values()]
    for i in range(len(a)):
        a[i]+=1
    
    for i in a:
        answer*=i
        
    return answer-1