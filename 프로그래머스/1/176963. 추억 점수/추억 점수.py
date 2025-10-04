def solution(name, yearning, photo):
    answer = []
    
    score_dict=dict()
    
    for i in range(len(name)):
        score_dict[name[i]]=yearning[i]
    
    for i in photo:
        total=0
        for j in i:
            if j not in score_dict.keys():
                continue
            total+=score_dict[j]
        answer.append(total)
    
    return answer