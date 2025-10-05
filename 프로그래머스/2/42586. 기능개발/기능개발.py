from collections import deque

def solution(progresses, speeds):
    answer = []
    days=deque()
    
    for i in range(len(progresses)):
        cnt=0    
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            cnt+=1
        days.append(cnt)
    
    stack=[]
    
    while days:
        if not answer:
            stack.append(days.popleft())
            answer.append(1)
        else:
            if stack[-1]>=days[0]:
                answer[-1]+=1
                days.popleft()
            else:
                answer.append(1)
                stack.append(days.popleft())
                
    print(answer)
    
    return answer