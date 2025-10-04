from collections import deque

def solution(s, skip, index):
    answer = ''
    
    a=deque('abcdefghijklmnopqrstuvwxyz')
    
    for i in skip:
        a.remove(i)
        
    for i in s:
        while a[0]!=i:
            a.append(a.popleft())
        
        for _ in range(index):
            a.append(a.popleft())
        
        answer+=a[0]
    
    return answer