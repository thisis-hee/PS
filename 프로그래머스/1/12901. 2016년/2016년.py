def solution(a, b):
    answer = 0
    
    # month_dict={'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30,
    #            'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31}
    
    month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_list = {1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED', 0:'THU'}
    
    for i in range(a-1):
        answer+=month_list[i]
        
    answer+=b
    answer=day_list[answer%7]
    return answer