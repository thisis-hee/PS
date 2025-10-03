def solution(s):
    answer = ''
    ord_list=[]
    for i in s:
        ord_list.append(ord(i))
    
    ord_list.sort(reverse=True)
    for i in ord_list:
        answer+=chr(i)
    
    return answer