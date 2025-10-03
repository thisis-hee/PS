def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        total=i
        j=i+1
        while total <= n :
            total+=j
            if total==n:
                answer+=1
                break
            j+=1
    
    answer+=1
    
    return answer