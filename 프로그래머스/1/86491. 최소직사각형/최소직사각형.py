def solution(sizes):
    new_sizes = []
    for i in sizes:
        new_sizes.append(sorted(i, reverse=True))
    
    max_x=0
    max_y=0
    
    for i in new_sizes:
        max_x=max(max_x, i[0])
        max_y=max(max_y, i[1])
    
    answer = max_x*max_y
    return answer