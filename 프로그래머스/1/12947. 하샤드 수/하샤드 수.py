def solution(x):
    answer = True
    
    x_list=list(map(int,list(str(x))))
    print(x_list)
    if x % sum(x_list) == 0:
        answer=True
    else:
        answer=False
    
    return answer