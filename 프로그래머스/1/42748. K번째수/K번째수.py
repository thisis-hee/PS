def solution(array, commands):
    
    answer = []
    
    for lst in commands:
        a=sorted(array[lst[0]-1:lst[1]])
        answer.append(a[lst[2]-1])
        
    return answer