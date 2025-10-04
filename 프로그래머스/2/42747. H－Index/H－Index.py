def solution(citations):
    answer = [0]
    
    for i in range(1, len(citations)+1):
        inyong = 0
        not_inyong = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                inyong += 1
        
        if inyong >= i:
            answer.append(i)
            
    answer = max(answer)
                
    return answer