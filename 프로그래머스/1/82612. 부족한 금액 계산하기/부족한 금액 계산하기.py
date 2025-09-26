def solution(price, money, count):
    result = price*count*(count+1)/2 - money
    
    if(result > 0):
        answer = result
    else:
        answer = 0
    
    return answer