from copy import deepcopy
from collections import deque

def solution(elements):
    answer = 0
    result_num=set()
    elements = deque(elements)
    elements2 = deepcopy(elements)
    chk = 1
    for i in range(len(elements)):
        for j in range(len(elements)):
            result_num.add(sum(list(elements)[:chk]))
            elements.append(elements.popleft())
        elements=elements2
        chk+=1
    
    answer = len(result_num)
            
    return answer