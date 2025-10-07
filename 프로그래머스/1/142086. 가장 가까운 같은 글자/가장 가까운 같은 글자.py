def solution(s):
    answer = []
    s_list=list(s)
    word_dict = {}
    
    for i in range(len(s_list)):
        if s_list[i] not in word_dict:
            word_dict[s_list[i]]=[-1,i]
            answer.append(-1)
        else:
            answer.append(i-word_dict[s_list[i]][1])
            word_dict[s_list[i]]=[-1,i]
    
    return answer