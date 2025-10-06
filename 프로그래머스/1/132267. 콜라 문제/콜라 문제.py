def solution(a, b, n):
    answer = 0
    
    while a<=n:
        answer += (n//a)*b
        full = (n//a)*b
        
        n%=a
        n+=full
    
    print(answer)
    
    return answer