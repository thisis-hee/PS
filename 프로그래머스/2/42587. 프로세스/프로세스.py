from collections import deque

def solution(priorities, location):
    answer = 0
    cnt=0
    priorities=deque(priorities)
    chk_deque=deque([x for x in range(len(priorities))])
    
    while priorities:
        if location not in chk_deque:
            break
        
        if priorities[0]!=max(priorities):
            priorities.append(priorities.popleft())
            chk_deque.append(chk_deque.popleft())
        else:
            cnt+=1
            priorities.popleft()
            chk_deque.popleft()
    
    answer=cnt
    
    return answer