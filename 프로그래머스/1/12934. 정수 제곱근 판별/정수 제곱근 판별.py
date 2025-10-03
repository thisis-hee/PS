import math

def solution(n):
    answer = 0
    
    if str(math.sqrt(n))[-1]=='0' and str(math.sqrt(n))[-2]=='.':
        return (int(math.sqrt(n))+1)**2
    else:
        return -1
    
    return answer