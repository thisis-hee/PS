def solution(s):
    
    str_list=s.split(' ')
    int_list=list(map(int, str_list))
    print(int_list)
    big = max(int_list)
    small = min(int_list)
    answer = str(small)+' '+str(big)
          
    return answer