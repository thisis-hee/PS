from collections import deque

def solution(answers):
    
    n1=deque([1,2,3,4,5])
    n2=deque([2,1,2,3,2,4,2,5])
    n3=deque([3,3,1,1,2,2,4,4,5,5])
    n1_correct=0
    n2_correct=0
    n3_correct=0
    
    for i in answers:
        n1.append(n1[0])
        n2.append(n2[0])
        n3.append(n3[0])
        if n1.popleft() == i:
            n1_correct+=1
        if n2.popleft() == i:
            n2_correct+=1
        if n3.popleft() == i:
            n3_correct+=1
        
    result = max(n1_correct, n2_correct, n3_correct)
    
    answer=[]
    
    if(n1_correct==result):
        answer.append(1)
    if(n2_correct==result):
        answer.append(2)
    if(n3_correct==result):
        answer.append(3)
    
    return answer