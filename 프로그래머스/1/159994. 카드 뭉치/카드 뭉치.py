from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1=deque(cards1)
    cards2=deque(cards2)
    
    for word in goal:
        if word in cards1:
            if cards1[0]!=word:
                return 'No'
            else:
                cards1.popleft()
            continue
        elif word in cards2:
            if cards2[0]!=word:
                return 'No'
            else:
                cards2.popleft()
    return answer